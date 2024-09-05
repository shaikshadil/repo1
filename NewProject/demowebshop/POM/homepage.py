from demowebshop.lib.library import Base

class HomePage(Base):
    login_link_locator =("xpath","//a[.='Log in']")
    resister_link_locator=("xpath","//a[.='Register']")
    search_link_locator = ("xpath","//input[@class='button-1 search-box-button']")
    def click_on_login(self):
        self.click_on_an_element(self.login_link_locator)
    def click_on_register(self):
        self.click_on_an_element(self.resister_link_locator)

    def click_on_search(self):
        self.click_on_an_element(self.search_link_locator)
