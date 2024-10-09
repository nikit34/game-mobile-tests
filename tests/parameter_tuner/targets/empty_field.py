from src.app.components.field_component import FieldComponent
from tests.parameter_tuner.feedbacks import feedback_cluster_within_bounds


class EmptyFieldTarget:
    TEST_DATA = (
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_1.png",
            "template_img": "app/elements/img/empty_field_element_1.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        },
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_2.png",
            "template_img": "app/elements/img/empty_field_element_1.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        },
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_3.png",
            "template_img": "app/elements/img/empty_field_element_1.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        },
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_1.png",
            "template_img": "app/elements/img/empty_field_element_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_2
        },
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_2.png",
            "template_img": "app/elements/img/empty_field_element_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_2
        },
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_3.png",
            "template_img": "app/elements/img/empty_field_element_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_2
        }
    )

    THRESHOLD_ERRORS = 180
    ERROR_CALLBACK = feedback_cluster_within_bounds
