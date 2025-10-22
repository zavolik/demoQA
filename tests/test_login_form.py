from pages.form_page import FormPage
import time

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)

# заполняем обязательные поля тестовыми данными
    form_page.first_name.send_keys('Ivan')
    form_page.last_name.send_keys('Petrov')
    form_page.user_email.send_keys('ipetro@gmail.com')
    form_page.gender_radio_1.click_force() # выбрали кнопку "male"
    form_page.user_number.send_keys('89119780278')
 # заполняем необязательные поля тестовыми данными
    form_page.hobbies_sports.click_force()
    form_page.current_address.send_keys('Saint-P')
    time.sleep(2)

    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()

# ElementClickInterceptedException - элемент еа странице не кликабельный, поэтому применяем click_force()
# теперь тест работает!

# как реализовать выбор страны на сайте (выпадающий список)
def test_state(browser) :
    form_page = FormPage(browser)
    form_page.visit()
    time.sleep (2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    form_page.btn_NCR.click()
    time.sleep(2)

