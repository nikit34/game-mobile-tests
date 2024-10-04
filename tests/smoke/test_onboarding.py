from pytest import mark

from src.app.elements.system_dialog_btn_element import SystemDialogBtnElement


@mark.usefixtures('driver', 'appium_service')
class TestOnboarding:
    def test_first_action(self, driver):
        SystemDialogBtnElement(driver, 2).is_visible().click()
