from appium.webdriver.common.appiumby import AppiumBy


class SystemDialogBtnElement:
    BUTTON_LOCATOR = (AppiumBy.ID, "com.playrix.township:id/system_dialog_button")

    def __init__(self, driver, button_index):
        self.driver = driver
        self.button_index = button_index

    def get_button_element(self):
        buttons = self.driver.find_elements(*self.BUTTON_LOCATOR)
        if 0 <= self.button_index < len(buttons):
            return buttons[self.button_index]
        else:
            raise IndexError("Button index out of range")

    def click(self):
        button = self.get_button_element()
        button.click()

