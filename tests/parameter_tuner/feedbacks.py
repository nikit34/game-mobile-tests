
def feedback_count_clusters(detected_clusters, expected_clusters):
    return abs(len(detected_clusters) - len(expected_clusters))
