from configs.images_checker_config import ImagesCheckerConfig
from tests.test_base import TestBase


def feedback_count_clusters(detected_clusters, expected_clusters):
    return abs(len(detected_clusters) - len(expected_clusters))


def feedback_cluster_within_bounds(detected_clusters, expected_clusters):
    tolerance = ImagesCheckerConfig.get_tolerance()

    if not detected_clusters:
        return float('inf')

    detected_clusters_sorted = sorted(detected_clusters, key=lambda cluster: cluster[0][0])
    expected_clusters_sorted = sorted(expected_clusters, key=lambda cluster: cluster[0][0])

    total_mismatch = 0

    for detected, expected in zip(detected_clusters_sorted, expected_clusters_sorted):
        if not TestBase._is_within_bounds(detected, expected, tolerance):
            total_mismatch += (
                    abs(detected[0][0] - expected[0][0]) +
                    abs(detected[0][1] - expected[0][1]) +
                    abs(detected[1][0] - expected[1][0]) +
                    abs(detected[1][1] - expected[1][1])
            )

    missing_clusters = abs(len(detected_clusters_sorted) - len(expected_clusters_sorted))
    total_mismatch += missing_clusters * 1000

    return total_mismatch
