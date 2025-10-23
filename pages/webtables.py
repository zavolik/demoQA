from components.components import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)

        self.no_data = WebElement (driver, "div.rt-noData")
        self.btn_delete_row = WebElement (driver, '[id^="delete-record-"]')

        self.btn_add = WebElement (driver, '#addNewRecordButton')
        self.dialog_box = WebElement(driver, "body > div.fade.modal.show > div > div > div.modal-body")
        self.btn_submit = WebElement (driver, '#submit')

        # элементы формы
        self.FirstName =  WebElement (driver, '#firstName')
        self.LastName = WebElement (driver, '#lastName')
        self.Email = WebElement (driver, '#userEmail')
        self.Age = WebElement (driver, '#age')
        self.Salary = WebElement (driver, '#salary')
        self.Department = WebElement (driver, '#department')

        self.cell_FirstName = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(1)')
        self.cell_LastName = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(2)')
        self.cell_Age = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(3)')
        self.cell_Email = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(4)')
        self.cell_Salary = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(5)')
        self.cell_Department = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(6)')
        self.searchBox = WebElement (driver, '#searchBox')
        self.btnSearch = WebElement (driver, '#basic-addon2')
        self.dialog_box_with_data = WebElement (driver, '#userForm')

    def pencilBtn_by_email(self, email: str):
        # Кнопка "редактировать" для строки с заданным email
        return WebElement(
            self.driver,
            f"//div[text()='{email}']/ancestor::div[@role='row']//span[@title='Edit']",
            locator_type='xpath'
        )

    def deleteBtn_by_email(self, email: str):
        # Кнопка "удалить" для строки с заданным email
        return WebElement(
            self.driver,
            f"//div[text()='{email}']/ancestor::div[@role='row']//span[@title='Delete']",
            locator_type='xpath'
        )
