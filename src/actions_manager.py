from configs.actions_config import ActionsConfig


class ActionsManager:
    def __init__(self, driver):
        self.driver = driver
        self.window_size = self.driver.get_window_size()
        self.duration = ActionsConfig.get_duration()

    def tap_by_coordinates(self, x, y):
        return self.driver.tap([(x, y)], self.duration)

    def swipe_down(self):
        start_x = end_x = self.window_size['width'] // 2
        start_y = self.window_size['height'] * 0.8
        end_y = self.window_size['height'] * 0.2

        return self.driver.swipe(start_x, start_y, end_x, end_y, self.duration)

    def swipe_up(self):
        start_x = end_x = self.window_size['width'] // 2
        start_y = self.window_size['height'] * 0.2
        end_y = self.window_size['height'] * 0.8

        return self.driver.swipe(start_x, start_y, end_x, end_y, self.duration)

    def scroll_vertical(self, start_y, end_y):
        start_x = end_x = self.window_size['width'] // 2

        return self.driver.swipe(start_x, start_y, end_x, end_y, self.duration)

    def scroll_horizontal(self, start_x, end_x):
        start_y = end_y = self.window_size['height'] // 2

        return self.driver.swipe(start_x, start_y, end_x, end_y, self.duration)
