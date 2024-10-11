from src.actions_manager import ActionsManager


class BaseOpencvElement:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_center_coordinates(x1, y1, x2, y2):
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        return center_x, center_y

    @staticmethod
    def _parse_coordinates(coordinates):
        if len(coordinates) == 2:
            (x1, y1), (x2, y2) = coordinates
        elif len(coordinates) == 1:
            (x1, y1), (x2, y2) = coordinates[0]
        elif len(coordinates) == 4:
            x1, y1, x2, y2 = coordinates
        else:
            raise ValueError("Incorrect coordinate format")
        return x1, y1, x2, y2

    def click(self, coordinates):
        x1, y1, x2, y2 = self._parse_coordinates(coordinates)
        x, y = self.get_center_coordinates(x1, y1, x2, y2)

        actions = ActionsManager(self.driver)
        actions.tap_by_coordinates(x, y)

    def drag_and_drop(self, coordinates_from, coordinates_to):
        start_x1, start_y1, start_x2, start_y2 = self._parse_coordinates(coordinates_from)
        end_x1, end_y1, end_x2, end_y2 = self._parse_coordinates(coordinates_to)

        start_x, start_y = self.get_center_coordinates(start_x1, start_y1, start_x2, start_y2)
        end_x, end_y = self.get_center_coordinates(end_x1, end_y1, end_x2, end_y2)

        actions = ActionsManager(self.driver)
        actions.drag_and_drop(start_x, start_y, end_x, end_y)

