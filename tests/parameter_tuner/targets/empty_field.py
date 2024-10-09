from src.app.components.field_component import FieldComponent
from tests.parameter_tuner.feedbacks import feedback_cluster_within_bounds


class EmptyFieldTarget:
    NAME_TARGET = "empty_field"

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
            "original_img": "screenshots/test_detection_4.png",
            "template_img": "app/elements/img/empty_field_element_1.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        },
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_5.png",
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
        },
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_4.png",
            "template_img": "app/elements/img/empty_field_element_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_2
        },
        {
            "target": "empty_field",
            "original_img": "screenshots/test_detection_5.png",
            "template_img": "app/elements/img/empty_field_element_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_2
        }
    )

    THRESHOLD_ERRORS = 180
    ERROR_CALLBACK = feedback_cluster_within_bounds

    PARAM_GRID = {
        "clahe_clip_limit": [5.0, 6.0],
        "clahe_grid_size": [[8, 1]],
        "contrast_threshold": [0.03, 0.04],
        "eps": [14, 15, 16],
        "min_cluster_area": [500],
        "min_samples": [4, 5],
        "n_octave_layers": [3],
        "ransac": [True],
        "ransac_threshold": [9, 10, 11]
    }
