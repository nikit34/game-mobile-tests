from src.image import Image
from src.image_detector import ImageDetector
from src.images_manager import ImagesManager


class TestDetection:
    def setup_method(self):
        images_manager = ImagesManager()
        images_manager.remove("temporary_images")

    def test_detection(self):
        screenshot_img = Image(path_image="screenshots/test.jpeg")

        yellow_arrow_down_img = Image(path_image="app/elements/img/yellow_arrow_down.png")
        coordinates = ImageDetector.get_coordinates_objects(screenshot_img, yellow_arrow_down_img)

        empty_field_1_img = Image(path_image="app/elements/img/empty_field_1.png")
        coordinates = ImageDetector.get_coordinates_objects(screenshot_img, empty_field_1_img)

        empty_field_2_img = Image(path_image="app/elements/img/empty_field_2.png")
        coordinates = ImageDetector.get_coordinates_objects(screenshot_img, empty_field_2_img)

        print(len(coordinates))