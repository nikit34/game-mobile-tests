from multiprocessing import Pool, Manager, cpu_count
from sklearn.model_selection import ParameterGrid
import json
from datetime import datetime

from src.files_manager import FilesManager
from src.image import Image
from src.image_detector import ImageDetector
from tests.parameter_tuner.feedbacks import feedback_cluster_within_bounds
from tests.parameter_tuner.test_data import test_data


class ParameterTuner:
    def __init__(self, image_detector_class, param_grid, threshold_errors):
        self.image_detector_class = image_detector_class
        self.param_grid = param_grid
        self.best_params = None
        self.best_total_error = float('inf')
        self.n_jobs = int(cpu_count() / 2)
        self.threshold_errors = threshold_errors

    @staticmethod
    def _save_params(params):
        with open('params_tuner/params_tuner-' + str(datetime.now()) + '.json', 'w') as f:
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
            print("Optimal parameters found with zero error: \n" + str(params))
            self._save_params(params)
            stop_flag.value = True

        return total_error, params

    def evaluate(self, test_data, error_callback):
        manager = Manager()
        stop_flag = manager.Value('i', False)

        with Pool(processes=self.n_jobs) as pool:
            results = []
            for params in ParameterGrid(self.param_grid):
                result = pool.apply_async(self.evaluate_single_param, (params, test_data, error_callback, stop_flag))
                results.append(result)

            pool.close()

            for result in results:
                total_error, params = result.get()

                if total_error is None:
                    continue

                if total_error < self.best_total_error:
                    self.best_total_error = total_error
                    self.best_params = params

                if stop_flag.value:
                    print("Zero error found, stopping further evaluations")
                    pool.terminate()
                    break

            pool.join()

        return self.best_params, self.best_total_error


if __name__ == "__main__":
    NEED_TEST_DATA_INDEXES = [0, 1, 2, 3]
    NEED_ERROR_CALLBACK = feedback_cluster_within_bounds
    THRESHOLD_ERRORS = 200

    param_grid = {
        "n_octave_layers": [3, 5, 15, 50],
        "contrast_threshold": [0.02, 0.04],
        "eps": [5, 10, 15, 20],
        "clahe_clip_limit": [5.0, 7.0, 9.0],
        "clahe_grid_size": [[8, 1], [8, 8]],
        "min_cluster_area": [500],
        "min_samples": [3, 5, 9],
        "ransac": [False, True],
        "ransac_threshold": [10]
    }

    files_manager = FilesManager()
    files_manager.remove("params_tuner")

    tuner = ParameterTuner(ImageDetector, param_grid, THRESHOLD_ERRORS)
    selected_test_data = [test_data[i] for i in NEED_TEST_DATA_INDEXES]
    best_params, best_total_error = tuner.evaluate(selected_test_data, NEED_ERROR_CALLBACK)
    print("Best overall params: \n" + str(best_params) + "\n with total error: " + str(best_total_error))
