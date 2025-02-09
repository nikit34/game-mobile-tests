from src.app.screens.polygons.components.field.field import FieldComponent
from src.app.elements.ernie import ErnieElement
from src.app.elements.wheat import WheatElement

TEST_DATA = [
    ("empty_field", "app/screens/polygons/img/empty_fields_ernie_0.png", "app/screens/polygons/components/field/elements/img/empty_field_1.png", FieldComponent.COORDINATES_FIELD_1),
    ("empty_field", "app/screens/polygons/img/empty_fields_ernie_1.png", "app/screens/polygons/components/field/elements/img/empty_field_1.png", FieldComponent.COORDINATES_FIELD_1),
    ("empty_field", "app/screens/polygons/img/empty_fields_ernie_2.png", "app/screens/polygons/components/field/elements/img/empty_field_1.png", FieldComponent.COORDINATES_FIELD_1),
    ("empty_field", "app/screens/polygons/img/empty_fields_ernie_3.png", "app/screens/polygons/components/field/elements/img/empty_field_1.png", FieldComponent.COORDINATES_FIELD_1),
    ("empty_field", "app/screens/polygons/img/empty_fields_ernie_4.png", "app/screens/polygons/components/field/elements/img/empty_field_1.png", FieldComponent.COORDINATES_FIELD_1),
    ("empty_field", "app/screens/polygons/img/empty_fields_ernie_0.png", "app/screens/polygons/components/field/elements/img/empty_field_2.png", FieldComponent.COORDINATES_FIELD_2),
    ("empty_field", "app/screens/polygons/img/empty_fields_ernie_1.png", "app/screens/polygons/components/field/elements/img/empty_field_2.png", FieldComponent.COORDINATES_FIELD_2),
    # ("empty_field", "app/screens/polygons/img/empty_fields_ernie_2.png", "app/screens/polygons/components/field/elements/img/empty_field_2.png", FieldComponent.COORDINATES_FIELD_2),
    ("empty_field", "app/screens/polygons/img/empty_fields_ernie_3.png", "app/screens/polygons/components/field/elements/img/empty_field_2.png", FieldComponent.COORDINATES_FIELD_2),
    ("empty_field", "app/screens/polygons/img/empty_fields_ernie_4.png", "app/screens/polygons/components/field/elements/img/empty_field_2.png", FieldComponent.COORDINATES_FIELD_2),
    ("ernie", "app/screens/polygons/img/empty_fields_ernie_0.png", "app/elements/img/ernie.png", ErnieElement.COORDINATES_ERNIE),
    ("ernie", "app/screens/polygons/img/empty_fields_ernie_1.png", "app/elements/img/ernie.png", ErnieElement.COORDINATES_ERNIE),
    ("ernie", "app/screens/polygons/img/empty_fields_ernie_2.png", "app/elements/img/ernie.png", ErnieElement.COORDINATES_ERNIE),
    ("ernie", "app/screens/polygons/img/empty_fields_ernie_3.png", "app/elements/img/ernie.png", ErnieElement.COORDINATES_ERNIE),
    ("ernie", "app/screens/polygons/img/empty_fields_ernie_4.png", "app/elements/img/ernie.png", ErnieElement.COORDINATES_ERNIE),
    ("wheat", "app/screens/polygons/img/wheat_0.png", "app/elements/img/wheat.png", WheatElement.COORDINATES_WHEAT),
    ("wheat_field", "app/screens/polygons/img/wheat_fields_0.png", "app/screens/polygons/components/field/elements/img/wheat_field_1.png", FieldComponent.COORDINATES_FIELD_1),
    ("wheat_field", "app/screens/polygons/img/wheat_fields_0.png", "app/screens/polygons/components/field/elements/img/wheat_field_2.png", FieldComponent.COORDINATES_FIELD_1),
]
