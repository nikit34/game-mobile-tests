from time import sleep

from pytest import mark

from src.actions_manager import ActionsManager
from src.app.screens.onboarding.components.game_center_component import GameCenterComponent
from src.app.elements.system_dialog_btn_element import SystemDialogBtnElement
from src.environment_manager import EnvironmentManager
from src.image import Image
from src.image_detector import ImageDetector
from src.screenshot import Screenshot


@mark.skip
@mark.usefixtures('driver', 'appium_service')
class TestOnboarding:
    def test_first_action(self, driver):
        EnvironmentManager.execute_ios_callback(
            lambda: GameCenterComponent(driver, GameCenterComponent.CLOSE_BTN).is_visible().click()
        )
        EnvironmentManager.execute_platform_specific_callback(
            lambda: SystemDialogBtnElement(driver, 2).is_visible().click(),
            lambda: SystemDialogBtnElement(driver).is_visible().click()
        )

        sleep(4)
        actions = ActionsManager(driver)
        actions.tap_by_coordinates(440, 250)
        sleep(2)

        screenshot = Screenshot(driver)
        screenshot_img = Image(image=screenshot.get_screenshot())

        yellow_arrow_down_img = Image(path_image="app/elements/img/yellow_arrow_down.png")
        coordinates = ImageDetector.get_coordinates_objects(screenshot_img, yellow_arrow_down_img)

        empty_field_1_img = Image(path_image="app/elements/img/empty_field_1.png")
        coordinates = ImageDetector.get_coordinates_objects(screenshot_img, empty_field_1_img)

        empty_field_2_img = Image(path_image="app/elements/img/empty_field_2.png")
        coordinates = ImageDetector.get_coordinates_objects(screenshot_img, empty_field_2_img)
