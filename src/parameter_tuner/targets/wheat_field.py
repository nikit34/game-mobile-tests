from src.app.screens.polygons.components.field.field import FieldComponent
from src.parameter_tuner.feedbacks import feedback_cluster_within_bounds


class WheatFieldTarget:
    NAME_TARGET = "wheat_field"

    TEST_DATA = (
        {
            "original_img": "app/screens/polygons/img/wheat_fields_0.png",
            "template_img": "app/screens/polygons/components/field/elements/img/wheat_field_1.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        },
        {
            "original_img": "app/screens/polygons/img/wheat_fields_0.png",
            "template_img": "app/screens/polygons/components/field/elements/img/wheat_field_2.png",
            "expected_clusters": FieldComponent.COORDINATES_FIELD_1
        }
    )

    THRESHOLD_ERRORS = 180
    MAX_ALLOWED_ERROR = 1000
    ERROR_CALLBACK = feedback_cluster_within_bounds

    PARAM_GRID = {
        "clahe_clip_limit": [2.0, 3.0, 4.0],
        "clahe_grid_size": [[1, 1], [8, 1]],
        "contrast_threshold": [0.04, 0.06, 0.08],
        "eps": [16, 18, 20],
        "min_cluster_area": [400, 500],
        "min_samples": [8, 10],
        "n_octave_layers": [3, 5],
        "ransac": [False, True],
        "ransac_threshold": [10]
    }