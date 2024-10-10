import pytest
from src.image.image import Image
from src.image.image_detector import ImageDetector
from tests.test_base import TestBase
from tests.test_data.detection import TEST_DATA


class TestDetection(TestBase):
    @pytest.mark.parametrize(
        "name_target, original_image_path, field_image_path, expected_clusters", TEST_DATA)
    def test_count_clusters(self, name_target, original_image_path, field_image_path, expected_clusters):
        image_detector = ImageDetector(name_target)
        original_img = Image(path_image=original_image_path, resize_image=True)
        template_img = Image(path_image=field_image_path)

        detected_clusters = image_detector.get_coordinates_objects(original_img, template_img)

        assert len(detected_clusters) == len(expected_clusters), "Number of clusters does not match."

    @pytest.mark.parametrize("name_target, original_image_path, field_image_path, expected_clusters", TEST_DATA)
    def test_cluster_within_bounds(self, name_target, original_image_path, field_image_path, expected_clusters):
        image_detector = ImageDetector(name_target)
        original_img = Image(path_image=original_image_path, resize_image=True)
        template_img = Image(path_image=field_image_path)

        detected_clusters = image_detector.get_coordinates_objects(original_img, template_img)

        self.check_clusters(detected_clusters, expected_clusters)
