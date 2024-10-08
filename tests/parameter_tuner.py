from sklearn.model_selection import ParameterGrid
from tqdm import tqdm

from src.app.components.field_component import FieldComponent
from src.app.elements.ernie_element import ErnieElement
from src.image import Image
from src.image_detector import ImageDetector
from src.images_manager import ImagesManager


class ParameterTuner:
    def __init__(self, image_detector, param_grid):
        self.image_detector = image_detector
        self.param_grid = param_grid
        self.best_params = None
        self.best_error = float('inf')

    def evaluate(self, original_img, template_img, expected_clusters):
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

            error = abs(len(detected_clusters) - len(expected_clusters))

            if error < self.best_error:
                self.best_error = error
                self.best_params = params

        return self.best_params, self.best_error


if __name__ == "__main__":
    images_manager = ImagesManager()
    images_manager.remove("temporary_images")

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

    test_data = (
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_1.png",
            "template_img": "app/elements/img/empty_field_element_1.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        },
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_2.png",
            "template_img": "app/elements/img/empty_field_element_1.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        },
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_1.png",
            "template_img": "app/elements/img/empty_field_element_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_2
        },
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_2.png",
            "template_img": "app/elements/img/empty_field_element_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_2
        },
        {
            "target": "ernie",
            "original_img": "screenshots/test_detection_1.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "target": "ernie",
            "original_img": "screenshots/test_detection_2.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        }
    )

    for test_item in test_data:

        image_detector = ImageDetector(test_item.get("target"))

        tuner = ParameterTuner(image_detector, param_grid)

        best_params, best_error = tuner.evaluate(
            original_img=lambda: Image(path_image=test_item.get("original_img")),
            template_img=lambda: Image(path_image=test_item.get("template_img")),
            expected_clusters=test_item.get("expected_clusters")
        )

        print("Best params: " + str(best_params) + " with error: " + str(best_error) + " for test data: " + str(test_item))
