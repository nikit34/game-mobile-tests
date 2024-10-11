from pytest import mark

from src.app.components.field_component import FieldComponent
from src.app.elements.ernie_element import ErnieElement
from src.app.elements.wheat_element import WheatElement
from src.app.screens.onboarding.components.game_center import GameCenterComponent
from src.app.elements.system_dialog_btn_element import SystemDialogBtnElement
from src.environment_manager import EnvironmentManager
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

        empty_field_detected_clusters = self.wait_load_clusters(
            screenshot,
            "app/elements/img/empty_field_element_1.png",
            "empty_field",
            FieldComponent.COORDINATES_FIELD_1
        )

        ernie_detected_clusters = self.wait_load_clusters(
            screenshot,
            "app/elements/img/ernie_element.png",
            "ernie",
            ErnieElement.COORDINATES_ERNIE
        )

        ErnieElement(driver).click(ernie_detected_clusters)
        FieldComponent(driver).click(empty_field_detected_clusters)

        wheat_detected_clusters = self.wait_load_clusters(
            screenshot,
            "app/elements/img/wheat_element.png",
            "wheat",
            WheatElement.COORDINATES_WHEAT
        )
        WheatElement(driver).drag_and_drop(wheat_detected_clusters, empty_field_detected_clusters)

        self.wait_load_clusters(
            screenshot,
            "app/screens/polygons/components/field/elements/img/wheat_field_1.png",
            "wheat",
            FieldComponent.COORDINATES_FIELD_1
        )


