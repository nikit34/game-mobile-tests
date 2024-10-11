from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from configs.actions_config import ActionsConfig


class ActionsManager:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.window_size = self.driver.get_window_size()
        self.duration = ActionsConfig.get_duration()
        self.default_move_factor = (0.2, 0.8)

    def tap_by_coordinates(self, x, y):
        self.actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        self.actions.w3c_actions.pointer_action.move_to_location(x, y) \
            .pointer_down() \
            .release()
        self.actions.perform()
        return self

    def swipe_down(self):
        start_x = end_x = self.window_size['width'] // 2
        start_y = self.window_size['height'] * self.default_move_factor[1]
        end_y = self.window_size['height'] * self.default_move_factor[0]

        self.driver.swipe(start_x, start_y, end_x, end_y, self.duration)
        return self

    def swipe_up(self):
        start_x = end_x = self.window_size['width'] // 2
        start_y = self.window_size['height'] * self.default_move_factor[0]
        end_y = self.window_size['height'] * self.default_move_factor[1]

        self.driver.swipe(start_x, start_y, end_x, end_y, self.duration)
        return self

    def scroll_vertical(self, start_y, end_y):
        start_x = end_x = self.window_size['width'] // 2

        self.driver.swipe(start_x, start_y, end_x, end_y, self.duration)
        return self

    def scroll_horizontal(self, start_x, end_x):
        start_y = end_y = self.window_size['height'] // 2

        self.driver.swipe(start_x, start_y, end_x, end_y, self.duration)
        return self

    def drag_and_drop(self, start_x, start_y, end_x, end_y):
        self.driver.flick(start_x, start_y, end_x, end_y)
        return self

