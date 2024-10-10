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
    ERROR_CALLBACK = feedback_cluster_within_bounds

    PARAM_GRID = {
        "clahe_clip_limit": [3.8, 4.0, 4.2],
        "clahe_grid_size": [[8, 1], [8, 2]],
        "contrast_threshold": [0.043, 0.045, 0.047],
        "eps": [15],
        "min_cluster_area": [550, 600, 650],
        "min_samples": [7, 8, 9],
        "n_octave_layers": [2, 3, 4],
        "ransac": [True],
        "ransac_threshold": [13]
    }

