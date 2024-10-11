from src.base_elements.base_opencv_element import BaseOpencvElement


class WheatElement(BaseOpencvElement):
    COORDINATES_WHEAT = (
        ((425, 325), (475, 390)),
    )

    def __init__(self, driver):
        super().__init__(driver)
