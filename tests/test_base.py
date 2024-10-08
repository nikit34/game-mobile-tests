from configs.images_checker_config import ImagesCheckerConfig
from src.image_detector import ImageDetector
from src.images_manager import ImagesManager


class TestBase:
    @classmethod
    def setup_class(cls):
        images_manager = ImagesManager()
        images_manager.remove("temporary_images")

        cls.tolerance = ImagesCheckerConfig.get_tolerance()
        cls.image_detector = ImageDetector()

    def is_within_bounds(self, cluster, expected_cluster):
        ((x_min1, y_min1), (x_max1, y_max1)) = cluster
        ((x_min2, y_min2), (x_max2, y_max2)) = expected_cluster

        return (
            abs(x_min1 - x_min2) <= self.tolerance and
            abs(y_min1 - y_min2) <= self.tolerance and
            abs(x_max1 - x_max2) <= self.tolerance and
            abs(y_max1 - y_max2) <= self.tolerance
        )

    def check_clusters(self, detected_clusters, expected_clusters):
        if not detected_clusters:
            raise AssertionError("No clusters were found")

        for detected, expected in zip(detected_clusters, expected_clusters):
            if not self.is_within_bounds(detected, expected):
                raise AssertionError("Cluster " + str(detected) + " is out of bounds " + str(expected))
