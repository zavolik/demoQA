import time
from pages.text_box import TextBox


def test_clear(browser):
    text_box = TextBox(browser)
    text_box.visit()
    text_box.full_name.send_keys("Alexandrina")
    time.sleep(2)

    text_box.full_name.clear()
    time.sleep(2)

    assert text_box.full_name.get_text() == ''
# проверяем, что поле пустое (сначала ввели имя, потом очистили поле)
