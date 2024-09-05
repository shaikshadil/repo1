import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver
from demowebshop.POM.homepage import HomePage

def attach_screenshot():
    allure.attach(driver.get_screenshot_as_png(), name="test_check_for_login", attachment_type=AttachmentType.PNG)


@pytest.fixture()
def driver():
    driver = WebDriver()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()

def test_check_for_login(driver):
    home_page_obj = HomePage(driver)
    home_page_obj.click_on_login()
    condition= driver.find_element("id","Email").is_displayed()
    if condition == False:
        attach_screenshot()
    assert condition
    allure.attach(driver.get_screenshot_as_png(),name="test_check_for_login",attachment_type=AttachmentType.PNG)

# def test_check_for_register(driver):
#     home_page_obj = HomePage(driver)
#     home_page_obj.click_on_register()

