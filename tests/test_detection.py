import pytest
from src.app.components.field_component import FieldComponent
from src.app.elements.ernie_element import ErnieElement
from src.image import Image
from src.image_detector import ImageDetector
from tests.test_base import TestBase


class TestDetection(TestBase):
    @pytest.mark.parametrize(
        "name_target, original_image_path, field_image_path, expected_clusters", [
        ("empty_field", "screenshots/test_detection_1.png", "app/elements/img/empty_field_element_1.png", FieldComponent.COORDINATES_FIELD_1),
        ("empty_field", "screenshots/test_detection_2.png", "app/elements/img/empty_field_element_1.png", FieldComponent.COORDINATES_FIELD_1),
        ("empty_field", "screenshots/test_detection_3.png", "app/elements/img/empty_field_element_1.png", FieldComponent.COORDINATES_FIELD_1),
        ("empty_field", "screenshots/test_detection_1.png", "app/elements/img/empty_field_element_2.png", FieldComponent.COORDINATES_FIELD_2),
        ("empty_field", "screenshots/test_detection_2.png", "app/elements/img/empty_field_element_2.png", FieldComponent.COORDINATES_FIELD_2),
        ("empty_field", "screenshots/test_detection_3.png", "app/elements/img/empty_field_element_2.png", FieldComponent.COORDINATES_FIELD_2),
        ("ernie", "screenshots/test_detection_1.png", "app/elements/img/ernie_element.png", ErnieElement.COORDINATES_ERNIE),
        ("ernie", "screenshots/test_detection_2.png", "app/elements/img/ernie_element.png", ErnieElement.COORDINATES_ERNIE),
        ("ernie", "screenshots/test_detection_3.png", "app/elements/img/ernie_element.png", ErnieElement.COORDINATES_ERNIE)
    ])
    def test_count_clusters(self, name_target, original_image_path, field_image_path, expected_clusters):
        image_detector = ImageDetector(name_target)
        original_img = Image(path_image=original_image_path, resize_image=True)
        template_img = Image(path_image=field_image_path)

        detected_clusters = image_detector.get_coordinates_objects(original_img, template_img)

        assert len(detected_clusters) == len(expected_clusters), "Number of clusters does not match."

    @pytest.mark.parametrize("name_target, original_image_path, field_image_path, expected_clusters", [
        ("empty_field", "screenshots/test_detection_1.png", "app/elements/img/empty_field_element_1.png", FieldComponent.COORDINATES_FIELD_1),
        ("empty_field", "screenshots/test_detection_2.png", "app/elements/img/empty_field_element_1.png", FieldComponent.COORDINATES_FIELD_1),
        ("empty_field", "screenshots/test_detection_3.png", "app/elements/img/empty_field_element_1.png", FieldComponent.COORDINATES_FIELD_1),
        ("empty_field", "screenshots/test_detection_1.png", "app/elements/img/empty_field_element_2.png", FieldComponent.COORDINATES_FIELD_2),
        ("empty_field", "screenshots/test_detection_2.png", "app/elements/img/empty_field_element_2.png", FieldComponent.COORDINATES_FIELD_2),
        ("empty_field", "screenshots/test_detection_3.png", "app/elements/img/empty_field_element_2.png", FieldComponent.COORDINATES_FIELD_2),
        ("ernie", "screenshots/test_detection_1.png", "app/elements/img/ernie_element.png", ErnieElement.COORDINATES_ERNIE),
        ("ernie", "screenshots/test_detection_2.png", "app/elements/img/ernie_element.png", ErnieElement.COORDINATES_ERNIE),
        ("ernie", "screenshots/test_detection_3.png", "app/elements/img/ernie_element.png", ErnieElement.COORDINATES_ERNIE)
    ])
    def test_cluster_within_bounds(self, name_target, original_image_path, field_image_path, expected_clusters):
        image_detector = ImageDetector(name_target)
        original_img = Image(path_image=original_image_path, resize_image=True)
        template_img = Image(path_image=field_image_path)

        detected_clusters = image_detector.get_coordinates_objects(original_img, template_img)

        self.check_clusters(detected_clusters, expected_clusters)
