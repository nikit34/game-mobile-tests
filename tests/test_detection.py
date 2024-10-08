import pytest
from src.app.components.field_component import FieldComponent
from src.image import Image
from tests.test_base import TestBase


class TestDetection(TestBase):
    @pytest.mark.parametrize("field_image_path, expected_clusters", [
        ("app/elements/img/empty_field_element_1.png", FieldComponent.COORDINATES_FIELD_1),
        ("app/elements/img/empty_field_element_2.png", FieldComponent.COORDINATES_FIELD_2)
    ])
    def test_count_clusters(self, field_image_path, expected_clusters):
        original_img = Image(path_image="screenshots/test_detection.png", resize_image=True)
        empty_field_img = Image(path_image=field_image_path)

        detected_clusters = self.image_detector.get_coordinates_objects(original_img, empty_field_img)

        assert len(detected_clusters) == len(expected_clusters), "Number of clusters does not match."

    @pytest.mark.parametrize("field_image_path, expected_clusters", [
        ("app/elements/img/empty_field_element_1.png", FieldComponent.COORDINATES_FIELD_1),
        ("app/elements/img/empty_field_element_2.png", FieldComponent.COORDINATES_FIELD_2)
    ])
    def test_cluster_within_bounds(self, field_image_path, expected_clusters):
        original_img = Image(path_image="screenshots/test_detection.png", resize_image=True)
        empty_field_img = Image(path_image=field_image_path)

        detected_clusters = self.image_detector.get_coordinates_objects(original_img, empty_field_img)

        self.check_clusters(detected_clusters, expected_clusters)