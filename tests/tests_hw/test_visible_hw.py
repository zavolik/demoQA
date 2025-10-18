from pages.accordian import Accordian # импортируйте новый класс
import time

def test_visible_accordian(browser):
    accordian_page = Accordian(browser) # создайте объект страницы

    accordian_page.visit() # перейти на страницу https://demoqa.com/accordian

    assert accordian_page.text_btn_what.visible() # проверьте, что элемент #section1Content > p виден

    accordian_page.btn_what.click()
    time.sleep(2)
#     assert not accordian_page.text_btn_what.visible()

def test_visible_accordian_default(browser):
    accordian_page = Accordian(browser) # создайте объект страницы

    accordian_page.visit() # перейти на страницу https://demoqa.com/accordian
    # проверьте, что следующие элементы по умолчанию скрыты
    assert not accordian_page.text_btn_where_1.visible()
    assert not accordian_page.text_btn_where_2.visible()
    assert not accordian_page.text_btn_why.visible()
