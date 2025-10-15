from pages.demoqa import DemoQa
from components.components import WebElement

# перейти на страницу 'https://demoqa.com/'
# проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’
def test_check_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    text_element = WebElement(browser, "#app > footer > span")

    expected_text = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."
    print("\ntext from element: " + text_element.get_text().strip())  # для самопроверки
    assert text_element.get_text().strip() == expected_text


# перейти на страницу 'https://demoqa.com/'
# через кнопку перейти на страницу 'https://demoqa.com/elements'
# проверить, что текст по центру == 'Please select an item from left to start practice.'
def test_check_center_footer(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    elements_card = WebElement(browser, "#app > div > div > div.home-body > div > div:nth-child(1)")
    assert elements_card.get_text() == "Elements"
    elements_card.click()
    center_text = WebElement(browser, "#app > div > div > div > div.col-12.mt-4.col-md-6")
    expected_text = "Please select an item from left to start practice."
    print("\ncenter text: " + center_text.get_text().strip()) # для самопроверки
    assert center_text.get_text().strip() == expected_text

