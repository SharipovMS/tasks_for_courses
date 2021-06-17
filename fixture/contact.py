from selenium.webdriver.support.select import Select
from model.contact import Contact
import re

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
        self.cont_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_cont_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_cont_page()
        self.cont_cache = None

    def count(self):
        wd = self.app.wd
        self.open_cont_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, test_create_contact_class):
        wd = self.app.wd
        self.open_cont_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("(//img[@alt='Edit'])")[index].click()
        #заполнение формы контакта
        self.fill_contact_form(test_create_contact_class)
        #обновление
        wd.find_element_by_name("update").click()
        self.open_cont_page()
        self.cont_cache = None

    cont_cache = None

    def get_contact_list(self):
        if self.cont_cache is None:
            wd = self.app.wd
            self.open_cont_page()
            self.cont_cache = [] #подготовили_список
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                print(firstname)
                address = cells[3].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.cont_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id, all_phones=all_phones, all_phones_from_home_page=all_phones, all_emails=all_emails))
        return list(self.cont_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_cont_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_cont_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)