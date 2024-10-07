from datetime import datetime
import os


class ScreenshotsManager:
    def __init__(self, driver):
        self.driver = driver
        self.current_dir = os.path.dirname(os.path.abspath(__file__))

    def save_screenshot(self, screenshot_name):
        file_path = os.path.join(self.current_dir, 'screenshots/', screenshot_name + "-" + str(datetime.now()) + ".png")
        self.driver.save_screenshot(file_path)

    def get_screenshot(self):
        return self.driver.get_screenshot_as_base64()
