from pages.modal_dialogs import ModalDialogs

#
# def test_modal_elements(browser):
#     page_dialogs = ModalDialogs(browser)
#     page_dialogs.visit()
#
#     assert page_dialogs.child_buttons.check_count_elements(count=5)
#     # проверить, что кнопок подменю на странице 5 шт

def test_navigation_modal(browser):
    page_dialogs = ModalDialogs(browser)
    page_dialogs.visit() # перейти на страницу https://demoqa.com/modal-dialogs
    page_dialogs.refresh() # обновить страницу

    page_dialogs.icon.click() # перейти на главную страницу через иконку
    browser.back() # сделать шаг назад стрелкой браузера (обращение к браузеру)
    browser.set_window_size(900, 400) # установить размеры экрана 900х400
    browser.forward() # сделать шаг вперед стрелкой браузера

    assert browser.title == 'DEMOQA' # проверить title на главной
    browser.set_window_size(1000, 1000) # вернуть размеры экрана по умолчанию 1000x1000


