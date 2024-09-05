# import openpyxl
import pytest
from utilities.excel_reader import get_list_from_excel
from demowebshop.POM.homepage import HomePage
from demowebshop.POM.loginpage import LogIn

# usernames=[("shadilshaik75@gmail.com","Shadil@123"),("abc@gmail.com",""),("xyz@gmail.com",""),("nop@gmail.com","")]

credentials= get_list_from_excel()
@pytest.mark.parametrize("username,password",credentials)
def test_login_with_proper_credentials(driver,username,password):
    home =HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application(username,password)
    assert driver.find_element("xpath",f"//a[.='{username}']").is_displayed()

@pytest.mark.skip
def test_login_with_invalid_credentials(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("shadil@gmail.com", "shadil546")
    assert driver.find_element("xpath","//div[@class='validation-summary-errors']").is_displayed()

@pytest.mark.skip
def test_login_with_no_credentials(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("", "")
    assert driver.find_element("xpath", "//div[@class='validation-summary-errors']").is_displayed()