from src.app.elements.ernie_element import ErnieElement
from tests.parameter_tuner.feedbacks import feedback_cluster_within_bounds


class ErnieTarget:
    NAME_TARGET = "ernie"

    TEST_DATA = [
        {
            "original_img": "screenshots/test_detection_0.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "original_img": "screenshots/test_detection_1.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "original_img": "screenshots/test_detection_2.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "original_img": "screenshots/test_detection_3.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "original_img": "screenshots/test_detection_4.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "original_img": "screenshots/test_detection_5.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        }
    ]

    THRESHOLD_ERRORS = 200
    ERROR_CALLBACK = feedback_cluster_within_bounds

    PARAM_GRID = {
        "clahe_clip_limit": [2.0, 3.0],
        "clahe_grid_size": [[1, 1], [5, 1]],
        "contrast_threshold": [0.01, 0.02],
        "eps": [30, 50],
        "min_cluster_area": [1000],
        "min_samples": [1, 3],
        "n_octave_layers": [2, 50],
        "ransac": [True, False],
        "ransac_threshold": [3, 5]
    }
