from _pytest.fixtures import fixture
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.appium_service import AppiumService

from configs.appium_config import AppiumConfig
from configs.desired_caps_config import DesiredCapsConfig
from configs.waiting_config import WaitingConfig


@fixture(scope='function')
def driver():
    desired_caps = DesiredCapsConfig.get_desired_caps()
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote("http://localhost:4723", options=capabilities_options)
    implicitly_timeout = WaitingConfig.get_implicitly_timeout()
    driver.implicitly_wait(implicitly_timeout)
    yield driver
    driver.quit()


@fixture(scope='session')
def appium_service():
    service = AppiumService()
    host = AppiumConfig.get_host()
    port = AppiumConfig.get_port()
    timeout = AppiumConfig.get_timeout()
    service.start(
        args=['--address', host, '-p', str(port)],
        timeout_ms=timeout,
    )
    yield service
    service.stop()
