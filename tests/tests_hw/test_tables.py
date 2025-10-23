import time
from pages.webtables import WebTables

def test_tables_btn_add(browser):
    page_tables = WebTables(browser)
    page_tables.visit()
    page_tables.btn_add.click()
    time.sleep(2)

    assert page_tables.dialog_box.exist() # проверяем, что по клику на кнопку Add открывается диалоговое окно
    page_tables.btn_submit.click()
    time.sleep(2)

    assert page_tables.dialog_box.exist() # в диалоге нельзя сохранить пустую форму: форма не закроется при нажатии на submit
    # заполняем форму построчно тестовыми данными
    page_tables.FirstName.send_keys('John')
    page_tables.LastName.send_keys('Doe')
    page_tables.Email.send_keys('JD23@mail.ru')
    page_tables.Age.send_keys('18')
    page_tables.Salary.send_keys('2000')
    page_tables.Department.send_keys('Department')

    page_tables.btn_submit.click()
    time.sleep(2)
    assert not page_tables.dialog_box.exist() # если заполнить все поля и нажать на кнопку Submit, диалог закрывается

    # проверяем, что в таблицу добавляется новая запись с введенными данными, для этого:
    page_tables.searchBox.send_keys('JD23@mail.ru')
    page_tables.btnSearch.click()
    time.sleep(6)
    assert (page_tables.cell_FirstName.get_text() == 'John'
            and page_tables.cell_LastName.get_text() == 'Doe'
            and page_tables.cell_Age.get_text() == '18'
            and page_tables.cell_Salary.get_text() == '2000'
            and page_tables.cell_Department.get_text() == 'Department'
            and page_tables.cell_Email.get_text() == 'JD23@mail.ru'
            )
    # если кликнуть на карандаш на строке записи, открывается диалог с введенными данными
    page_tables.pencilBtn_by_email("JD23@mail.ru").click() # сделала динамический локатор, завязанный на e-mail
    # фиксированный локатор меняется при смене строки, это нам не подходит - такая проверка уже не пройдет
    assert page_tables.dialog_box_with_data.exist()
    page_tables.FirstName.clear() # очистили, чтобы не получить 'JohnSam'
    page_tables.FirstName.send_keys('Sam')
    page_tables.btn_submit.click()
    time.sleep(2)
    # если изменить имя и сохранить, то в таблице обновятся данные
    assert (page_tables.cell_FirstName.get_text() == 'Sam'
            and page_tables.cell_LastName.get_text() == 'Doe'
            and page_tables.cell_Age.get_text() == '18'
            and page_tables.cell_Salary.get_text() == '2000'
            and page_tables.cell_Department.get_text() == 'Department'
            and page_tables.cell_Email.get_text() == 'JD23@mail.ru'
            )

    # если нажать на корзину в строке записи - запись удаляется
    page_tables.deleteBtn_by_email("JD23@mail.ru").click()
    time.sleep(2)
    assert page_tables.no_data.exist()