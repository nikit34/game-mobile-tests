from src.app.elements.wheat_element import WheatElement
from src.parameter_tuner.feedbacks import feedback_cluster_within_bounds


class WheatTarget:
    NAME_TARGET = "wheat"

    TEST_DATA = [
        {
            "original_img": "app/screens/polygons/wheat_0.png",
            "template_img": "app/elements/img/wheat_element.png",
            "expected_clusters": WheatElement.COORDINATES_WHEAT
        }
    ]

    THRESHOLD_ERRORS = 50
    ERROR_CALLBACK = feedback_cluster_within_bounds

    PARAM_GRID = {
        "clahe_clip_limit": [1.0, 2.0],
        "clahe_grid_size": [[1, 1], [8, 1]],
        "contrast_threshold": [0.01, 0.04],
        "eps": [10, 13, 15],
        "min_cluster_area": [400, 500],
        "min_samples": [1, 4, 9],
        "n_octave_layers": [3, 5, 10],
        "ransac": [True, False],
        "ransac_threshold": [2, 4]
    }