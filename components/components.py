from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys # можно передавать действие клавиш с клавиатуры (delite, control...)

class WebElement:
    def __init__(self, driver, locator="", locator_type='css'):
        self.locator = locator
        self.driver = driver
        self.locator_type = locator_type

    def click(self):
        self.find_element().click()

    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element()) # зеленым передали JS-код

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self): # поиск элементов по неуникальному локатору
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def check_css(self, style, value=''):
        return self.find_element().value_of_css_property(style) == value

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def visible(self):
        return self.find_element().is_displayed()

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    def send_keys(self,text:str): # метод для ввода текста
        self.find_element().send_keys(text)

    def clear(self):
        self.find_element().send_keys(Keys.COMMAND + 'a')
        self.find_element().send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)
        if value is None:
            return False # если такого атрибута нет
        if len(value) > 0:
            return value
        return True

    def get_by_type(self): # получаем возможность искать по любому локатору - мультипоиск
        if self.locator_type == "id":
            return By.ID
        elif self.locator_type == "name":
            return By.NAME
        elif self.locator_type == "xpath":
            return By.XPATH
        elif self.locator_type == "css":
            return By.CSS_SELECTOR
        elif self.locator_type == "class":
            return By.CLASS_NAME
        elif self.locator_type == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + self.locator_type + " not correct")
        return False

    def scroll_to_element(self): # скроллить страницу до нужного элемента
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);",
            self.find_element()
        )

