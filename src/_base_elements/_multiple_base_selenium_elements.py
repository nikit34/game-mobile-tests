from selenium.common import NoSuchElementException

from src._base_elements._base_selenium_element import BaseSeleniumElement


class BaseSeleniumElements(BaseSeleniumElement):
    def __init__(self, driver, locator, index=0):
        super().__init__(driver, locator)
        self.driver = driver
        self.locator = locator
        self.index = index
        self.elements = []

    def get_elements(self):
        if not self.elements:
            self.elements = self.driver.find_elements(*self.locator)
        return self.elements

    def get_element(self):
        elements = self.get_elements()
        if 0 <= self.index < len(elements):
            return elements[self.index]
        else:
            raise IndexError("Element index out of range")

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
