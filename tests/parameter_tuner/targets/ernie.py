from src.app.elements.ernie_element import ErnieElement
from tests.parameter_tuner.feedbacks import feedback_cluster_within_bounds


class ErnieTarget:
    NAME_TARGET = "ernie"

    COUNT_POLYGONS = 4
    TEST_DATA = [
        {
            "target": "ernie",
            "original_img": "screenshots/test_detection_" + str(i) + ".png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        }
        for i in range(COUNT_POLYGONS)
    ]

    THRESHOLD_ERRORS = 200
    ERROR_CALLBACK = feedback_cluster_within_bounds

    PARAM_GRID = {
        "clahe_clip_limit": [3.0, 5.0],
        "clahe_grid_size": [[6, 1], [8, 1]],
        "contrast_threshold": [0.02, 0.09],
        "eps": [13, 20],
        "min_cluster_area": [800],
        "min_samples": [3, 8],
        "n_octave_layers": [2, 10],
        "ransac": [True, False],
        "ransac_threshold": [5, 10]
    }
