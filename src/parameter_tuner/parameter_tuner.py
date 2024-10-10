import os
from multiprocessing import Pool, Manager, cpu_count
from sklearn.model_selection import ParameterGrid
import json
from datetime import datetime

from tqdm import tqdm

from src.file_manager import FileManager
from src.image.image import Image
from src.image.image_detector import ImageDetector
from src.parameter_tuner.targets.ernie import ErnieTarget
from src.parameter_tuner.targets.empty_field import EmptyFieldTarget



class ParameterTuner:
    def __init__(self, image_detector_class, name_target, param_grid, error_callback, threshold_errors, max_allowed_error):
        self.image_detector_class = image_detector_class
        self.name_target = name_target
        self.param_grid = param_grid
        self.best_params = None
        self.best_total_error = float('inf')
        self.n_jobs = int(cpu_count() / 2)
        self.error_callback = error_callback
        self.threshold_errors = threshold_errors
        self.max_allowed_error = max_allowed_error

    @staticmethod
    def _save_params(params, name_target, move_to_configs=False):
        if params is not None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, 'tmp_params', name_target + '-' + str(datetime.now()) + '.json')
            with open(file_path, 'w') as f:
                json.dump(params, f, indent=4)
            if move_to_configs:
                two_levels_up_current_dir = os.path.dirname(os.path.dirname(current_dir))
                file_path = os.path.join(
                    two_levels_up_current_dir, 'configs', 'json', 'images', 'detection_parameters', name_target + '.json'
                )
                with open(file_path, 'w') as f:
                    json.dump(params, f, indent=4)

    def evaluate_single_param(self, params, test_data, stop_flag):
        if stop_flag.value:
            return None, None

        total_error = -1
        for test_item in tqdm(test_data):
            image_detector = self.image_detector_class(self.name_target, save_img=False)
            image_detector.n_octave_layers = params['n_octave_layers']
            image_detector.contrast_threshold = params['contrast_threshold']
            image_detector.eps = params['eps']
            image_detector.clahe_clip_limit = params['clahe_clip_limit']
            image_detector.clahe_grid_size = params['clahe_grid_size']
            image_detector.min_cluster_area = params['min_cluster_area']
            image_detector.min_samples = params['min_samples']
            image_detector.ransac = params['ransac']
            image_detector.ransac_threshold = params['ransac_threshold']

            original_img = Image(path_image=test_item.get("original_img"), resize_image=True)
            template_img = Image(path_image=test_item.get("template_img"))

            detected_clusters = image_detector.get_coordinates_objects(original_img, template_img)
            error = self.error_callback(detected_clusters, test_item.get("expected_clusters"))
            total_error += error

            if total_error > self.max_allowed_error:
                print("Skipping parameters due to high error: " + str(total_error) + " > " + str(self.max_allowed_error))
                return float('inf'), params

        if total_error <= self.threshold_errors and total_error != -1:
            print("Optimal parameters found: \n" + str(params) + "\nWith total error: " + str(total_error))
            self._save_params(params, self.name_target)
            stop_flag.value = True

        return total_error, params

    def evaluate(self, test_data):
        manager = Manager()
        stop_flag = manager.Value('i', False)

        param_grid = list(ParameterGrid(self.param_grid))
        test_data_shared = manager.list(test_data)

        with Pool(processes=self.n_jobs) as pool:
            results = pool.starmap(
                self.evaluate_single_param,
                [(
                    params,
                    test_data_shared,
                    stop_flag
                ) for params in param_grid]
            )

            for result in results:
                total_error, params = result

                if total_error is None or total_error == float('inf'):
                    continue

                if total_error < self.best_total_error and total_error != -1:
                    self.best_total_error = total_error
                    self.best_params = params

        return self.best_params, self.best_total_error


if __name__ == "__main__":
    TARGET = EmptyFieldTarget

    file_manager = FileManager()
    file_manager.remove("parameter_tuner/tmp_params")

    tuner = ParameterTuner(ImageDetector, TARGET.NAME_TARGET, TARGET.PARAM_GRID, TARGET.ERROR_CALLBACK, TARGET.THRESHOLD_ERRORS, TARGET.MAX_ALLOWED_ERROR)
    best_params, best_total_error = tuner.evaluate(TARGET.TEST_DATA)
    if best_total_error == -1:
        print("Model found nothing")
    elif best_params is not None:
        print("Best parameters found: \n" + str(best_params) + "\nWith total error: " + str(best_total_error))
        ParameterTuner._save_params(best_params, TARGET.NAME_TARGET, move_to_configs=True)