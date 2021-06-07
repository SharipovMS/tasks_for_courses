from selenium.webdriver.support.select import Select
from model.test_create_contact_class import class_for_test_create_contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_edit_page(self):
        # открытие главной страницы
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_cont_page(self):
        # открытие главной страницы
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_list_value(self, filed_date, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(filed_date).click()
            Select(wd.find_element_by_name(filed_date)).select_by_visible_text(text)

    def fill_contact_form(self, test_create_contact_class):
        wd = self.app.wd
        self.change_field_value("firstname", test_create_contact_class.firstname)
        self.change_field_value("middlename", test_create_contact_class.second_name)
        self.change_field_value("lastname", test_create_contact_class.lastname)
        self.change_field_value("nickname", test_create_contact_class.nickname)
        self.change_field_value("company", test_create_contact_class.company)
        self.change_field_value("address", test_create_contact_class.address)
        self.change_field_value("home", test_create_contact_class.home)
        self.change_field_value("mobile", test_create_contact_class.mobile)
        self.change_field_value("work", test_create_contact_class.work)
        self.change_field_value("fax", test_create_contact_class.fax)
        self.change_field_value("email", test_create_contact_class.email)
        self.change_field_value("email2", test_create_contact_class.email2)
        self.change_field_value("email3", test_create_contact_class.email3)
        self.change_field_value("homepage", test_create_contact_class.homepage)
        self.change_list_value("bday", test_create_contact_class.bday)
        self.change_list_value("bmonth", test_create_contact_class.bmonth)
        self.change_field_value("byear", test_create_contact_class.byear)
        self.change_field_value("address2", test_create_contact_class.address2)
        self.change_field_value("dom", test_create_contact_class.dom)
        self.change_field_value("notes", test_create_contact_class.notes)

    def create(self, test_create_contact_class):
        # Заполнение формы адресной книги
        wd = self.app.wd
        self.open_edit_page()
        self.fill_contact_form(test_create_contact_class)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_cont_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_cont_page()

    def count(self):
        wd = self.app.wd
        self.open_cont_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self, test_create_contact_class):
        wd = self.app.wd
        self.open_cont_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//img[@alt='Edit'])[1]").click()
        #заполнение формы контакта
        self.fill_contact_form(test_create_contact_class)
        #обновление
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def get_contact_list(self):
        wd = self.app.wd
        self.open_cont_page()
        contacts = [] #подготовили_список
        for element in wd.find_elements_by_css_selector("tr[name=entry]"): #цикл в котором ищутся все элементы среди
            text = element.text #текс
            id = element.find_element_by_name("selected[]").get_attribute("value") #значения валуе
            contacts.append(class_for_test_create_contact(firstname=text, id=id))
        return contacts