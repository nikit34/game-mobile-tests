from src.app.elements.ernie import ErnieElement
from src.parameter_tuner.feedbacks import feedback_cluster_within_bounds


class ErnieTarget:
    NAME_TARGET = "ernie"

    TEST_DATA = [
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_0.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_1.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_2.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_3.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_4.png",
            "template_img": "app/elements/img/ernie_element.png",
            "expected_clusters": ErnieElement.COORDINATES_ERNIE
        }
    ]

    THRESHOLD_ERRORS = 200
    MAX_ALLOWED_ERROR = 1000
    ERROR_CALLBACK = feedback_cluster_within_bounds

    PARAM_GRID = {
        "clahe_clip_limit": [1.0],
        "clahe_grid_size": [[1, 1], [8, 1]],
        "contrast_threshold": [0.01],
        "eps": [13],
        "min_cluster_area": [1000],
        "min_samples": [1, 4, 9],
        "n_octave_layers": [3, 5, 10],
        "ransac": [True, False],
        "ransac_threshold": [2]
    }
