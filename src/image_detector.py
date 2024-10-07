import cv2
import numpy as np


class ImageDetector:
    @staticmethod
    def get_coordinates_objects(original_img, template_img):
        if original_img.cv_image.ndim == 2:
            original_img.cv_image = cv2.cvtColor(original_img.cv_image, cv2.COLOR_GRAY2BGR)
        if template_img.cv_image.ndim == 2:
            template_img.cv_image = cv2.cvtColor(template_img.cv_image, cv2.COLOR_GRAY2BGR)

        result = cv2.matchTemplate(original_img.cv_image, template_img.cv_image, cv2.TM_CCOEFF_NORMED)

        threshold = 0.6
        yloc, xloc = np.where(result >= threshold)

        coordinates_dict = {}

        _, w, h = template_img.cv_image.shape[::-1]
        for index, (x, y) in enumerate(zip(xloc, yloc)):
            cv2.rectangle(original_img.cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            coordinates_dict[f"Object {index + 1}"] = {"x": x, "y": y}

        original_img.save_image("detected")
        template_img.save_image("template")
