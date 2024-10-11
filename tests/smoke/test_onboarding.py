from pytest import mark

from src.app.components.field_component import FieldComponent
from src.app.elements.ernie_element import ErnieElement
from src.app.elements.wheat_element import WheatElement
from src.app.screens.onboarding.components.game_center import GameCenterComponent
from src.app.elements.system_dialog_btn_element import SystemDialogBtnElement
from src.environment_manager import EnvironmentManager
from src.image.image import Image
from src.image.image_detector import ImageDetector
from src.image.screenshot import Screenshot
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

        screenshot = Screenshot(driver)

        @self.wait_load()
        def wait_load_clusters(screenshot, template_path_img, name_target, expected_clusters):
            screenshot_img = screenshot.get_screenshot()
            original_img = Image(image=screenshot_img, resize_image=True)
            template_img = Image(path_image=template_path_img)
            image_detector = ImageDetector(name_target)
            detected_clusters = image_detector.get_coordinates_objects(original_img, template_img)
            self.check_clusters(detected_clusters, expected_clusters)
            return detected_clusters

        empty_field_detected_clusters = wait_load_clusters(
            screenshot,
            "app/elements/img/empty_field_element_1.png",
            "empty_field",
            FieldComponent.COORDINATES_FIELD_1
        )

        ernie_detected_clusters = wait_load_clusters(
            screenshot,
            "app/elements/img/ernie_element.png",
            "ernie",
            ErnieElement.COORDINATES_ERNIE
        )

        ErnieElement(driver).click(ernie_detected_clusters)
        FieldComponent(driver).click(empty_field_detected_clusters)

        wheat_detected_clusters = wait_load_clusters(
            screenshot,
            "app/elements/img/wheat_element.png",
            "wheat",
            WheatElement.COORDINATES_WHEAT
        )
        WheatElement.drag_and_drop(wheat_detected_clusters, empty_field_detected_clusters)




