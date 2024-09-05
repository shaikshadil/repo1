from demowebshop.POM.homepage import HomePage
class RegisterPage(HomePage):
    gender_locator=("id","gender-male")
    firstname_locator=("id","FirstName")
    lastname_locator = ("id","LastName")
    email1_locator = ("id","Email")
    password_locator=("id","Password")
    confirfmpassword_locator=("id","ConfirmPassword")
    register_btn=("xpath","//input[@class='button-1 register-next-step-button']")

    def register_to_the_application(self,firstname,lastname,username,password,confirmpassword):
        self.click_on_an_element(self.gender_locator)
        self.send_text_to_an_element(self.firstname_locator,firstname)
        self.send_text_to_an_element(self.lastname_locator,lastname)
        self.send_text_to_an_element(self.email1_locator,username)
        self.send_text_to_an_element(self.password_locator,password)
        self.send_text_to_an_element(self.confirfmpassword_locator,confirmpassword)
        self.click_on_an_element(self.register_btn)