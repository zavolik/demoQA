from pages.elements_page import ElementsPage

def test_find_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()

    assert elements_page.btns_first_menu.check_count_elements(count=9)
# проверка, что с таким локатором "div:nth-child(1) > div > ul > li" есть 9 элементов на странице "https://demoqa.com/elements"
