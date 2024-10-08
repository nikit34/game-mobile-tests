from sklearn.model_selection import ParameterGrid
from tqdm import tqdm

from src.image import Image
from src.image_detector import ImageDetector
from src.images_manager import ImagesManager
from tests.parameter_tuner.feedbacks import feedback_count_clusters
from tests.parameter_tuner.test_data import test_data


class ParameterTuner:
    def __init__(self, image_detector, param_grid):
        self.image_detector = image_detector
        self.param_grid = param_grid
        self.best_params = None
        self.best_error = float('inf')

    def evaluate(self, original_img, template_img, expected_clusters, error_callback):
        for params in tqdm(ParameterGrid(self.param_grid)):
            self.image_detector.n_octave_layers = params['n_octave_layers']
            self.image_detector.contrast_threshold = params['contrast_threshold']
            self.image_detector.eps = params['eps']
            self.image_detector.clahe_clip_limit = params['clahe_clip_limit']
            self.image_detector.clahe_grid_size = params['clahe_grid_size']
            self.image_detector.min_cluster_area = params['min_cluster_area']
            self.image_detector.min_samples = params['min_samples']
            self.image_detector.ransac = params['ransac']
            self.image_detector.ransac_threshold = params['ransac_threshold']

            detected_clusters = image_detector.get_coordinates_objects(original_img(), template_img())

            error = error_callback(detected_clusters, expected_clusters)
            if error < self.best_error:
                self.best_error = error
                self.best_params = params

            if not error:
                break

        return self.best_params, self.best_error


if __name__ == "__main__":
    NEED_TEST_DATA_INDEXES = [0]
    NEED_ERROR_CALLBACK = feedback_count_clusters
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

    images_manager = ImagesManager()
    images_manager.remove("temporary_images")

    selected_test_data = [test_data[i] for i in NEED_TEST_DATA_INDEXES]
    for test_item in selected_test_data:
        image_detector = ImageDetector(test_item.get("target"))
        tuner = ParameterTuner(image_detector, param_grid)
        best_params, best_error = tuner.evaluate(
            original_img=lambda: Image(path_image=test_item.get("original_img")),
            template_img=lambda: Image(path_image=test_item.get("template_img")),
            expected_clusters=test_item.get("expected_clusters"),
            error_callback=NEED_ERROR_CALLBACK
        )

        print("Best params: " + str(best_params) + " with error: " + str(best_error) + " for test data: " + str(test_item))
