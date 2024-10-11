from appium.webdriver.common.appiumby import AppiumBy

from configs.desired_caps_config import DesiredCapsConfig
from src._base_elements._multiple_base_selenium_elements import BaseSeleniumElements
from src.environment_manager import EnvironmentManager


class SystemDialogBtnElement(BaseSeleniumElements):
    OK_BTN = EnvironmentManager.execute_platform_specific_callback(
        lambda: (AppiumBy.ID, DesiredCapsConfig.get_package_name() + ":id/system_dialog_button"),
        lambda: (AppiumBy.ACCESSIBILITY_ID, "OK")
    )

    def __init__(self, driver, index=0):
        super().__init__(driver, self.OK_BTN, index)

