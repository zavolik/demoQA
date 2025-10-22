from components.components import WebElement
from pages.base_page import BasePage


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)

        self.no_data = WebElement (driver, "div.rt-noData")
        self.btn_delete_row = WebElement (driver, "#delete-record- > svg > path")

