from _pytest.fixtures import fixture
from appium.options.android import UiAutomator2Options
from appium import webdriver

from configs.desired_caps_config import DesiredCapsConfig
from configs.waiting_config import WaitingConfig


@fixture(scope='function')
def driver(request):
    desired_caps = DesiredCapsConfig.get_desired_caps()
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote("http://localhost:4723", options=capabilities_options)
    implicitly_timeout = WaitingConfig.get_implicitly_timeout()
    driver.implicitly_wait(implicitly_timeout)
    yield driver
    driver.quit()
