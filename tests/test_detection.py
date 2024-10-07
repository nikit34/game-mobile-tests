import pytest
from src.app.components.field_component import FieldComponent
from src.image import Image
from src.images_manager import ImagesManager
from tests.test_base import TestBase


class TestDetection(TestBase):
    @staticmethod
    def setup_method():
        images_manager = ImagesManager()
        images_manager.remove("temporary_images")

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

        self.check_clusters(detected_clusters, expected_clusters)