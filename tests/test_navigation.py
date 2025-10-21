from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_navigation(browser): # тест-кейс
    demo_qa_page = DemoQa(browser) # создан объект класса страницы DemoQa
    elements_page = ElementsPage(browser) # создан объект класса страницы ElementsPage

    demo_qa_page.visit() # от объекта вызовите метод входа
    demo_qa_page.btn_elements.click()

    demo_qa_page.refresh() # вызвать обновление страницы от объекта страницы
    browser.refresh() # вызвать обновление страницы от browser
    browser.back()
    browser.forward()


    assert elements_page.equal_url() # от объекта страницы ElementsPage вызвать .equal_url()
