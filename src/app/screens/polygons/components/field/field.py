from src.base_elements.base_opencv_element import BaseOpencvElement


class FieldComponent(BaseOpencvElement):
    COORDINATES_FIELD_1 = (
        ((470, 150), (540, 190)),
        ((420, 230), (490, 280)),
    )

    COORDINATES_FIELD_2 = (
        ((480, 220), (540, 240)),
        ((350, 220), (430, 240)),
        ((540, 190), (590, 220)),
        ((420, 190), (480, 220)),
    )

    def __init__(self, driver):
        super().__init__(driver)

