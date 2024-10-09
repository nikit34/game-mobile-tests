from src.app.elements.ernie_element import ErnieElement
from tests.parameter_tuner.feedbacks import feedback_cluster_within_bounds


class ErnieTarget:
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
        }
    )

    THRESHOLD_ERRORS = 200
    ERROR_CALLBACK = feedback_cluster_within_bounds