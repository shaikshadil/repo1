# from demowebshop.POM.homepage import HomePage
# from demowebshop.POM.registerpage import RegisterPage
#
# def test_register_with_proper_credentials(driver):
#     home =HomePage(driver)
#     home.click_on_register()
#     register = RegisterPage(driver)
#     register.register_to_the_application("shadil","basha","shadilshaik75@gmail.com","Shadil@1234","Shadil@1234")
#     assert driver.find_element("xpath","//li[.='The specified email already exists']").is_displayed()
#
# def test_register_with_no_fname(driver):
#     home =HomePage(driver)
#     home.click_on_register()
#     register = RegisterPage(driver)
#     register.register_to_the_application("","basha","shadilshaik75@gmail.com","Shadil@1234","Shadil@1234")
#     assert driver.find_element("xpath","//span[.='First name is required.']").is_displayed()
#
# def test_register_with_no_lname(driver):
#     home =HomePage(driver)
#     home.click_on_register()
#     register = RegisterPage(driver)
#     register.register_to_the_application("shadil","","shadilshaik75@gmail.com","Shadil@1234","Shadil@1234")
#     assert driver.find_element("xpath","//span[.='Last name is required.']").is_displayed()
#
# def test_register_with_no_email(driver):
#     home =HomePage(driver)
#     home.click_on_register()
#     register = RegisterPage(driver)
#     register.register_to_the_application("shadil","basha","","Shadil@1234","Shadil@1234")
#     assert driver.find_element("xpath","//span[.='Email is required.']").is_displayed()
#
# def test_register_with_no_improperemail(driver):
#     home =HomePage(driver)
#     home.click_on_register()
#     register = RegisterPage(driver)
#     register.register_to_the_application("shadil","basha","shadil@.com","Shadil@1234","Shadil@1234")
#     assert driver.find_element("xpath","//span[.='Wrong email']").is_displayed()
#
# def test_register_with_no_password(driver):
#     home =HomePage(driver)
#     home.click_on_register()
#     register = RegisterPage(driver)
#     register.register_to_the_application("shadil","basha","","","Shadil@1234")
#     assert driver.find_element("xpath","//span[.='Password is required.']").is_displayed()
#
# def test_register_with_no_credentials(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = RegisterPage(driver)
#     register.register_to_the_application("", "", "", "", "")
#     assert driver.find_element("xpath", "//span[.='First name is required.']").is_displayed() and driver.find_element("xpath", "//span[.='Last name is required.']").is_displayed()and driver.find_element("xpath", "//span[.='Email is required.']").is_displayed()and driver.find_element("xpath", "//span[.='Password is required.']").is_displayed() and driver.find_element("xpath", "//span[.='Password is required.']").is_displayed()
