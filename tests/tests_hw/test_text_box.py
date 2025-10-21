from pages.text_box import TextBox
# 1
def test_text_box(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()

    # просьба вводить данные через переменные
    name = 'Мария'
    result_name = 'Name:'+name
    address = 'Москва'
    result_address = 'Current Address :'+address

    text_box_page.full_name.send_keys(name)
    text_box_page.current_address.send_keys(address)
    text_box_page.submit_button.click_force()

    assert text_box_page.get_name() == result_name
    assert text_box_page.get_address() == result_address


