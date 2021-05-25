from selenium.webdriver.support.select import Select

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        # открытие главной страницы
        wd = self.app.wd
        wd.get("https://localhost/addressbook/")

    def open_page_group(self):
        wd = self.app.wd
        # Открытие страницы группы
        wd.find_element_by_link_text("groups").click()

    def check_page_group(self):
        wd = self.app.wd
        # Проверка страницы группы
        wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        wd = self.app.wd
        # выбор первой группы
        wd.find_element_by_name("selected[]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        #проверка значения
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        # Ввод данных в форму
        self.open_page_group()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.check_page_group()

    # Изменение первой группы
    def mod_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_page_group()
        self.select_first_group()
        #открыть форму редактирования
        wd.find_element_by_name("edit").click()
        #заполненеи форм группы
        self.fill_group_form(new_group_data)
        #обновить данные
        wd.find_element_by_name("update").click()
        self.check_page_group()


    #Удаление первой группы
    def delete_first_group(self):
        wd = self.app.wd
        self.open_page_group()
        #выбрать первую группу
        wd.find_element_by_name("selected[]").click()
        #удалить группу
        wd.find_element_by_name("delete").click()
        self.check_page_group()