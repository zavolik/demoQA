from pages.text_box import TextBox

def test_placeholder(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit() # перейти на страницу https://demoqa.com/text-box
    assert text_box_page.full_name.get_dom_attribute('placeholder') == 'Full Name'
# обращаемся к атрибуту placeholder, который есть у элемента full_name и проверяем его значение - совпадение с 'Full Name'
