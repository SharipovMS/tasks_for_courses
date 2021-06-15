from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        # открытие главной страницы
        wd = self.app.wd
        wd.get("https://localhost/addressbook/")

    def open_page_group(self):
        wd = self.app.wd
        #проверка_требуется_ли_переход_по_ссылке
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
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
        self.group_cache = None

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0)

    # Изменение случайной группы
    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_page_group()
        self.select_group_by_index(index)
        #открыть форму редактирования
        wd.find_element_by_name("edit").click()
        #заполненеи форм группы
        self.fill_group_form(new_group_data)
        #обновить данные
        wd.find_element_by_name("update").click()
        self.check_page_group()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    #Удаление первой группы
    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_page_group()
        self.select_group_by_index(index)
        #удалить группу
        wd.find_element_by_name("delete").click()
        self.check_page_group()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_page_group()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_page_group()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)