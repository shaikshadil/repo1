from demowebshop.POM.homepage import HomePage

class SearchObject(HomePage):
    searchfield =("xpath","//input[@class='search-box-text ui-autocomplete-input']")
    search_btn=("xpath","//input[@class='button-1 search-box-button']")

    def search_an_object(self,searchtext):
        self.send_text_to_an_element(self.searchfield,searchtext)
        self.click_on_an_element(self.search_btn)


