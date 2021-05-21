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

    def create(self, group):
        wd = self.app.wd
        # Ввод данных в форму
        self.open_page_group()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.check_page_group()

    #Удаление первой группы
    def delete_first_group(self):
        wd = self.app.wd
        self.open_page_group()
        #выбрать первую группу
        wd.find_element_by_name("selected[]").click()
        #удалить группу
        wd.find_element_by_name("delete").click()

    # Изменение первой группы
    def mod_first_group(self, group):
        wd = self.app.wd
        self.open_page_group()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("update").click()
        self.check_page_group()