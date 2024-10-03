from _pytest.fixtures import fixture
from appium.options.android import UiAutomator2Options
from appium import webdriver


@fixture(scope='function')
def driver(request):
    desired_caps = {
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:noReset": False,
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.playrix.township",
        "appium:appActivity": "com.playrix.township.Launcher"
    }
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote("http://localhost:4723", options=capabilities_options)
    yield driver
    driver.quit()
