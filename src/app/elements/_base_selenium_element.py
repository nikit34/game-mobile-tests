from selenium.common import NoSuchElementException


class BaseSeleniumElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = None

    def get_element(self):
        if self.element is None:
            self.element = self.driver.find_element(*self.locator)
        return self.element

    def click(self):
        element = self.get_element()
        element.click()
        return self

    def is_visible(self):
        element = self.get_element()
        if element.is_displayed():
            return self
        else:
            raise NoSuchElementException("Element is not visible")
