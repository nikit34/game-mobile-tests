from src.app.components.field_component import FieldComponent
from src.parameter_tuner.feedbacks import feedback_cluster_within_bounds


class EmptyFieldTarget:
    NAME_TARGET = "empty_field"

    TEST_DATA = (
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_0.png",
            "template_img": "app/elements/img/empty_field_element_1.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_1.png",
            "template_img": "app/elements/img/empty_field_element_1.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_2.png",
            "template_img": "app/elements/img/empty_field_element_1.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_3.png",
            "template_img": "app/elements/img/empty_field_element_1.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_4.png",
            "template_img": "app/elements/img/empty_field_element_1.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_0.png",
            "template_img": "app/elements/img/empty_field_element_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_2
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_1.png",
            "template_img": "app/elements/img/empty_field_element_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_2
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_2.png",
            "template_img": "app/elements/img/empty_field_element_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_2
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_3.png",
            "template_img": "app/elements/img/empty_field_element_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_2
        },
        {
            "original_img": "app/screens/polygons/empty_fields_ernie_4.png",
            "template_img": "app/elements/img/empty_field_element_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_2
        }
    )

    THRESHOLD_ERRORS = 180
    MAX_ALLOWED_ERROR = 1000
    ERROR_CALLBACK = feedback_cluster_within_bounds

    PARAM_GRID = {
        "clahe_clip_limit": [2.0, 3.0],
        "clahe_grid_size": [[1, 1]],
        "contrast_threshold": [0.06, 0.08],
        "eps": [18, 20],
        "min_cluster_area": [400, 500],
        "min_samples": [10, 12],
        "n_octave_layers": [3],
        "ransac": [False],
        "ransac_threshold": [10]
    }

