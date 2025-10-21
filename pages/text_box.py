from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):
    driver = ""
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/text-box"
        self.driver = driver
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName') # поле для ввода имени пользователя
        self.current_address = WebElement(driver,'#currentAddress')
        self.submit_button = WebElement(driver, '#submit')

    def get_name(self):
        return WebElement(self.driver, '#name').get_text()

    def get_address(self):
        return WebElement(self.driver, '#currentAddress.mb-1').get_text()
