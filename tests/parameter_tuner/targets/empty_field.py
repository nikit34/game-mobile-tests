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

    PARAM_GRID = {
        "n_octave_layers": [2, 3, 4],
        "contrast_threshold": [0.04, 0.05],
        "eps": [13, 15, 17],
        "clahe_clip_limit": [4.0, 5.0],
        "clahe_grid_size": [[8, 1], [8, 2]],
        "min_cluster_area": [500],
        "min_samples": [5, 6],
        "ransac": [True],
        "ransac_threshold": [5, 10]
    }
