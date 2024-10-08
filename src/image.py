import base64
import os
from datetime import datetime

import numpy as np
import cv2
from pathlib import Path

from configs.device_config import DeviceConfig
from src.files_manager import FilesManager


def resize(func):
    def wrapper(self, *args, **kwargs):
        image = func(self, *args, **kwargs)
        if image is None:
            raise ValueError("No image loaded to resize")

        if self.resize_image:
            device_appium_config = DeviceConfig("iPhone 11")

            target_width, target_height = device_appium_config.get_width(), device_appium_config.get_height()
            current_height, current_width = image.shape[:2]

            if current_width != target_width or current_height != target_height:
                image = cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_AREA)
        return image
    return wrapper


class Image(FilesManager):
    def __init__(self, image=None, path_image=None, flags=cv2.IMREAD_GRAYSCALE, resize_image=False):
        super().__init__()
        self.resize_image = resize_image
        self.cv_image = self._load_image(image, path_image, flags)

    @resize
    def _load_image(self, image, path_image, flags):
        if isinstance(image, str):
            return self._decode_base64_image(image, flags)
        elif isinstance(image, Path):
            return cv2.imread(str(image), flags)
        elif isinstance(path_image, str):
            full_path = str(os.path.join(self.current_dir, path_image))
            return cv2.imread(str(full_path), flags)
        else:
            raise TypeError("Input should be a base64 string or Path object with path to image file")

    @staticmethod
    def _decode_base64_image(base64_string, flags):
        decoded_image = base64.b64decode(base64_string)
        image_array = np.frombuffer(decoded_image, dtype=np.uint8)
        return cv2.imdecode(image_array, flags=flags)

    def save(self, name_image):
        if self.cv_image is None:
            raise ValueError("No image loaded to save")
        full_path = str(os.path.join(self.current_dir, "temporary_images/", name_image + "-" + str(datetime.now()) + ".png"))
        cv2.imwrite(full_path, self.cv_image)

