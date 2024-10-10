from src.actions_manager import ActionsManager


class BaseOpencvElement:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_center_coordinates(x1, y1, x2, y2):
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        return center_x, center_y

    def click(self, coordinates):
        (x1, y1), (x2, y2) = coordinates
        actions = ActionsManager(self.driver)
        x, y = self.get_center_coordinates(x1, y1, x2, y2)
        actions.tap_by_coordinates(x, y)

