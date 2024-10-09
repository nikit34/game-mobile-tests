from multiprocessing import Pool, Manager, cpu_count
from sklearn.model_selection import ParameterGrid
import json
from datetime import datetime
from tqdm import tqdm
from src.files_manager import FilesManager
from src.image import Image
from src.image_detector import ImageDetector
from tests.parameter_tuner.targets.empty_field import EmptyFieldTarget
from tests.parameter_tuner.targets.ernie import ErnieTarget


class ParameterTuner:
    def __init__(self, image_detector_class, param_grid, threshold_errors):
        self.image_detector_class = image_detector_class
        self.param_grid = param_grid
        self.best_params = None
        self.best_total_error = float('inf')
        self.n_jobs = int(cpu_count() / 2)
        self.threshold_errors = threshold_errors

    @staticmethod
    def _save_params(params, move_to_configs=False, name_target=None):
        with open('params_tuner/params_tuner-' + str(datetime.now()) + '.json', 'w') as f:
            json.dump(params, f, indent=4)
        if move_to_configs and name_target is not None:
            with open('../configs/json/images_detectors/' + name_target + '.json', 'w') as f:
                json.dump(params, f, indent=4)

    def evaluate_single_param(self, params, test_data, error_callback, stop_flag):
        if stop_flag.value:
            return None, None

        total_error = 0
        for test_item in test_data:
            image_detector = self.image_detector_class(test_item.get("target"), save_img=False)
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
            error = error_callback(detected_clusters, test_item.get("expected_clusters"))
            total_error += error

        if total_error <= self.threshold_errors:
            print("Optimal parameters found: \n" + str(params) + "\nWith total error: " + str(total_error))
            self._save_params(params)
            stop_flag.value = True

        return total_error, params

    def evaluate(self, test_data, error_callback):
        manager = Manager()
        stop_flag = manager.Value('i', False)

        param_grid = list(ParameterGrid(self.param_grid))
        test_data_shared = manager.list(test_data)

        with Pool(processes=self.n_jobs) as pool:
            results = pool.starmap(self.evaluate_single_param, [(params, test_data_shared, error_callback, stop_flag) for params in param_grid])

            for result in tqdm(results):
                total_error, params = result

                if total_error is None:
                    continue

                if total_error < self.best_total_error:
                    self.best_total_error = total_error
                    self.best_params = params

                if stop_flag.value:
                    print("Zero error found, stopping further evaluations")
                    break

        return self.best_params, self.best_total_error


if __name__ == "__main__":
    TARGET = EmptyFieldTarget

    files_manager = FilesManager()
    files_manager.remove("params_tuner")

    tuner = ParameterTuner(ImageDetector, TARGET.PARAM_GRID, TARGET.THRESHOLD_ERRORS)
    selected_test_data = TARGET.TEST_DATA
    best_params, best_total_error = tuner.evaluate(selected_test_data, TARGET.ERROR_CALLBACK)
    print("Optimal parameters found: \n" + str(best_params) + "\nWith total error: " + str(best_total_error))
    ParameterTuner._save_params(best_params, move_to_configs=True, name_target=TARGET.NAME_TARGET)