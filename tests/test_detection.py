import pytest
from src.app.components.field_component import FieldComponent
from src.image import Image
from src.image_detector import ImageDetector
from src.images_manager import ImagesManager

class TestDetection:
    @classmethod
    def setup_class(cls):
        cls.tolerance = 40
        cls.image_detector = ImageDetector()

    @staticmethod
    def setup_method():
        images_manager = ImagesManager()
        images_manager.remove("temporary_images")

    def is_within_bounds(self, cluster, expected_cluster):
        ((x_min1, y_min1), (x_max1, y_max1)) = cluster
        ((x_min2, y_min2), (x_max2, y_max2)) = expected_cluster

        return (
            abs(x_min1 - x_min2) <= self.tolerance and
            abs(y_min1 - y_min2) <= self.tolerance and
            abs(x_max1 - x_max2) <= self.tolerance and
            abs(y_max1 - y_max2) <= self.tolerance
        )

    @pytest.mark.parametrize("field_image_path, expected_clusters", [
        ("app/elements/img/empty_field_1.png", FieldComponent.COORDINATES_FIELD_1),
        ("app/elements/img/empty_field_2.png", FieldComponent.COORDINATES_FIELD_2)
    ])
    def test_count_clusters(self, field_image_path, expected_clusters):
        screenshot_img = Image(path_image="screenshots/test_detection.jpeg", resize_image=True)
        empty_field_img = Image(path_image=field_image_path)

        detected_clusters = self.image_detector.get_coordinates_objects(screenshot_img, empty_field_img)

        assert len(detected_clusters) == len(expected_clusters), "Number of clusters does not match."

    @pytest.mark.parametrize("field_image_path, expected_clusters", [
        ("app/elements/img/empty_field_1.png", FieldComponent.COORDINATES_FIELD_1),
        ("app/elements/img/empty_field_2.png", FieldComponent.COORDINATES_FIELD_2)
    ])
    def test_cluster_within_bounds(self, field_image_path, expected_clusters):
        screenshot_img = Image(path_image="screenshots/test_detection.jpeg", resize_image=True)
        empty_field_img = Image(path_image=field_image_path)

        detected_clusters = self.image_detector.get_coordinates_objects(screenshot_img, empty_field_img)

        for detected, expected in zip(detected_clusters, expected_clusters):
            assert self.is_within_bounds(detected, expected), "Cluster " + str(detected) + " is out of bounds " + str(expected)
