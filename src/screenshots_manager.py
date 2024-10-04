import os


class ScreenshotsManager:
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, screenshot_name):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'screenshots/', screenshot_name + '.png')
        self.driver.save_screenshot(file_path)
