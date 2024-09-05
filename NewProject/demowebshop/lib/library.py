from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
class Base:
    def __init__(self,driver):
        self.driver=driver
        ''

    def wait_for_visibility(self,locator, timeout):
        wait = WebDriverWait(self.driver, timeout)
        condition = visibility_of_element_located(locator)
        element = wait.until(condition)
        return element

    def search_for_an_element(self,locator):
        element = self.driver.find_element(*locator)
        return element

    def click_on_an_element(self,locator):
       element = self.driver.find_element(*locator)
       element.click()

    def double_click_on_an_element(self,locator):
        actions = ActionChains(self.driver)
        element = self.search_for_an_element(*locator)
        actions.double_click(element)

    def send_text_to_an_element(self,locator,text):
        element=self.search_for_an_element(locator)
        element.send_keys(text444)