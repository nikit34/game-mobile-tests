from configs.images_checker_config import ImagesCheckerConfig


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
        if not _is_within_bounds(detected, expected, tolerance):
            total_mismatch += (
                    abs(detected[0][0] - expected[0][0]) +
                    abs(detected[0][1] - expected[0][1]) +
                    abs(detected[1][0] - expected[1][0]) +
                    abs(detected[1][1] - expected[1][1])
            )

    missing_clusters = abs(len(detected_clusters_sorted) - len(expected_clusters_sorted))
    total_mismatch += missing_clusters * 1000

    return total_mismatch


def _is_within_bounds(cluster, expected_cluster, tolerance):
    ((x_min1, y_min1), (x_max1, y_max1)) = cluster
    ((x_min2, y_min2), (x_max2, y_max2)) = expected_cluster

    return (
            abs(x_min1 - x_min2) <= tolerance and
            abs(y_min1 - y_min2) <= tolerance and
            abs(x_max1 - x_max2) <= tolerance and
            abs(y_max1 - y_max2) <= tolerance
    )
