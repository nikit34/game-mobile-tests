from src.app.components.field_component import FieldComponent
from src.app.elements.ernie_element import ErnieElement

test_data = (
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