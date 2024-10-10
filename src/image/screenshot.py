from datetime import datetime
import os

from src.file_manager import FileManager


class Screenshot(FileManager):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def save(self, screenshot_name):
        file_path = os.path.join(self.current_dir, "image", "tmp_screenshots", screenshot_name + "-" + str(datetime.now()) + ".png")
        self.driver.save_screenshot(file_path)

    def get_screenshot(self):
        return self.driver.get_screenshot_as_base64()
