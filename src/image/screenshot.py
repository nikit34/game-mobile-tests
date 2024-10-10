from datetime import datetime
import os

import cv2

from configs.device_config import DeviceConfig
from src.file_manager import FileManager
from src.image.image import Image


class Screenshot(FileManager):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def save(self, screenshot_name):
        screenshot_base64 = self.get_screenshot()
        img = Image.decode_base64_image(screenshot_base64, flags=cv2.IMREAD_COLOR)

        device_config = DeviceConfig("iPhone 11")
        resolution = (device_config.get_width(), device_config.get_height())
        resized_img = cv2.resize(img, resolution)

        file_path = os.path.join(self.current_dir, "image", "tmp_screenshots", screenshot_name + "-" + str(datetime.now()) + ".png")
        cv2.imwrite(str(file_path), resized_img)

    def get_screenshot(self):
        return self.driver.get_screenshot_as_base64()
