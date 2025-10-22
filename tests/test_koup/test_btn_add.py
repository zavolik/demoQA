from pages import koup_add
from pages.koup import Koup
from pages.koup_add import KoupAdd

def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)
    koup_page.visit()

    assert koup_page.link_add.get_text() == 'Add/Remove Elements'
    koup_page.link_add.click()
    assert koup_add.equal_url() # суть проверки: по клику откроется та же ссылка, что заложена нами в файле koup_add.py
    assert koup_add.btn_add.get_text() == 'Add Element'
    assert koup_add.btn_add.get_dom_attribute('onclick') == "addElement()"

    # кликнуть по кнопке add element 4 раза
    for i in range(4):
        koup_add.btn_add.click()

    assert koup_add.btns_delete.check_count_elements(4) # после нажатия на кнопку add element появляются кнопки delete

    # проверка для всех элементов
    for element in koup_add.btns_delete.find_elements():
        assert element.text == 'Delete'

     # проверка только для первого элемента
    assert koup_add.btns_delete.get_text() == 'Delete'

    while koup_add.btns_delete.exist():
        koup_add.btns_delete.click()
    assert not koup_add.btns_delete.exist() # проверили, что удалили все кнопки Delete
