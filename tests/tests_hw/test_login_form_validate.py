from pages.form_page import FormPage
from selenium.webdriver.common.by import By

def test_login_form_validate(browser):
    form_page = FormPage(browser)
    form_page.visit() # перейти на страницу https://demoqa.com/automation-practice-form

    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert form_page.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    form_page.btn_submit.click_force()

    form_element = browser.find_element(By.TAG_NAME, 'form')
    class_attr = form_element.get_attribute('class')
    assert 'was-validated' in class_attr