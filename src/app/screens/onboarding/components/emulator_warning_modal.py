from src._base_elements._base_opencv_element import BaseOpencvElement


class EmulatorWarningComponent(BaseOpencvElement):
    KEEP_USING_EMULATOR_BTN = (562, 413, 737, 454)

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click(self):
        super().click(*self.KEEP_USING_EMULATOR_BTN)
