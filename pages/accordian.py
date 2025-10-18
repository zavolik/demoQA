from pages.base_page import BasePage
from components.components import WebElement

class Accordian(BasePage):


    def __init__(self, driver):
        self.base_url = "https://demoqa.com/accordian"
        super().__init__(driver, self.base_url)

        self.text_elements = WebElement(driver, "#accordianContainer > h1")
        self.icon = WebElement(driver, "header > a > img")
        self.btn_sidebar_elements = WebElement(driver, "#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(1) > span > div")
        self.btn_sidebar_forms = WebElement(driver, "#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(2) > span > div")
        self.btn_sidebar_alerts = WebElement(driver, "#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > span > div")
        self.btn_sidebar_widgets = WebElement(driver, "#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(4) > span > div")
        self.btn_sidebar_interactions = WebElement(driver, "#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(5) > span > div")
        self.btn_sidebar_book_store_app = WebElement(driver, "#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(6) > span > div")

        self.btn_what = WebElement(driver, "#section1Heading")
        self.text_btn_what = WebElement(driver, "#section1Content > p")
        self.btn_where = WebElement(driver, "#section2Heading")
        self.text_btn_where_1 = WebElement(driver, "#section2Content > p:nth-child(1)") # проверка
        self.text_btn_where_2 = WebElement(driver, "#section2Content > p:nth-child(2)") # проверка
        self.btn_why = WebElement(driver, "#section3Heading")
        self.text_btn_why = WebElement(driver, "#section3Content > p") # проверка
