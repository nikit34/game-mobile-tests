from _pytest.fixtures import fixture
from appium.options.android import UiAutomator2Options
from appium import webdriver

from configs.config import Config


@fixture(scope='function')
def driver(request):
    desired_caps = Config.get_desired_caps()
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote("http://localhost:4723", options=capabilities_options)
    implicitly_timeout = Config.get_implicitly_timeout()
    driver.implicitly_wait(implicitly_timeout)
    yield driver
    driver.quit()
