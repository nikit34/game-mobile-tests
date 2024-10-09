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
        "n_octave_layers": [2, 3],
        "contrast_threshold": [0.02, 0.03],
        "eps": [13],
        "clahe_clip_limit": [2.0, 3.0],
        "clahe_grid_size": [[6, 1], [7, 1]],
        "min_cluster_area": [600, 700],
        "min_samples": [3, 4],
        "ransac": [True, False],
        "ransac_threshold": [4, 5]
    }
