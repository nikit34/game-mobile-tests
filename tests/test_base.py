from configs.images_checker_config import ImagesCheckerConfig
from src.image_detector import ImageDetector


class TestBase:
    @classmethod
    def setup_class(cls):
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
        for detected, expected in zip(detected_clusters, expected_clusters):
            assert self.is_within_bounds(detected, expected), "Cluster " + str(detected) + " is out of bounds " + str(expected)
