from src._base_elements._base_opencv_element import BaseOpencvElement


class ErnieElement(BaseOpencvElement):
    COORDINATES_ERNIE = (
        ((50, 250), (140, 390)),
    )
    
    def __init__(self, driver):
        super().__init__(driver)
