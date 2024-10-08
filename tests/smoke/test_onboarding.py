from time import sleep

from pytest import mark

from src.actions_manager import ActionsManager
from src.app.components.field_component import FieldComponent
from src.app.elements.ernie_element import ErnieElement
from src.app.screens.onboarding.components.game_center_component import GameCenterComponent
from src.app.elements.system_dialog_btn_element import SystemDialogBtnElement
from src.environment_manager import EnvironmentManager
from src.image import Image
from src.screenshot import Screenshot
from tests.test_base import TestBase
from tests.conftest import driver, appium_service


@mark.usefixtures('appium_service', 'driver')
class TestOnboarding(TestBase):

    def test_first_action(self, driver):
        EnvironmentManager.execute_ios_callback(
            lambda: GameCenterComponent(driver, GameCenterComponent.CLOSE_BTN).is_visible().click()
        )
        EnvironmentManager.execute_platform_specific_callback(
            lambda: SystemDialogBtnElement(driver, 2).is_visible().click(),
            lambda: SystemDialogBtnElement(driver).is_visible().click()
        )

        sleep(4)
        screenshot = Screenshot(driver)
        screenshot_img = screenshot.get_screenshot()
        original_img = Image(image=screenshot_img, resize_image=True)

        empty_field_1_img = Image(path_image="app/elements/img/empty_field_element_1.png")
        detected_clusters = self.image_detector.get_coordinates_objects(original_img, empty_field_1_img)
        expected_clusters = FieldComponent.COORDINATES_FIELD_1
        self.check_clusters(detected_clusters, expected_clusters)

        empty_field_2_img = Image(path_image="app/elements/img/empty_field_element_2.png")
        detected_clusters = self.image_detector.get_coordinates_objects(original_img, empty_field_2_img)
        expected_clusters = FieldComponent.COORDINATES_FIELD_2
        self.check_clusters(detected_clusters, expected_clusters)

        ernie_img = Image(path_image="app/elements/img/ernie_element.png")
        detected_clusters = self.image_detector.get_coordinates_objects(original_img, ernie_img)
        expected_clusters = ErnieElement.COORDINATES_ERNIE
        self.check_clusters(detected_clusters, expected_clusters)
