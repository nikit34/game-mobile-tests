from src.app.elements.ernie_element import ErnieElement
from tests.parameter_tuner.feedbacks import feedback_cluster_within_bounds


class ErnieTarget:
    NAME_TARGET = "ernie"

    TEST_DATA = (
        {
            "target": "ernie",
            "original_img": "screenshots/test_detection_1.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "target": "ernie",
            "original_img": "screenshots/test_detection_2.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "target": "ernie",
            "original_img": "screenshots/test_detection_3.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "target": "ernie",
            "original_img": "screenshots/test_detection_4.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "target": "ernie",
            "original_img": "screenshots/test_detection_5.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        }
    )

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
