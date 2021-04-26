# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from task_three_class import Task_three_class
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        self.open_page(wd)
        self.auth_page(wd)
        self.create_person_data(wd, Task_three_class(firstname="Marat", second_name="Sharipov", lastname="Sericbaevich", nickname="murena", company="quality-lab", address="Moscow",
                                mobile="+7 906 523 43 03", home="-", work="-", email="murenashark@mail.ru", fax="-", email2="-", homepage="-", email3="-", bday="15",
                                bmonth="January", byear="1994", address2="Kostroma", dom="50", notes="Russia"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_person_data(self, wd, task_three_class):
        # Заполнение формы адресной книги
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(task_three_class.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(task_three_class.second_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(task_three_class.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(task_three_class.nickname)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(task_three_class.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(task_three_class.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(task_three_class.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(task_three_class.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(task_three_class.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(task_three_class.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(task_three_class.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(task_three_class.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(task_three_class.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(task_three_class.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(task_three_class.bday)
        wd.find_element_by_xpath("//option[@value='15']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(task_three_class.bmonth)
        wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(task_three_class.byear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(task_three_class.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(task_three_class.dom)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(task_three_class.notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def auth_page(self, wd, login="admin", password="secret"):
        # Авторизация
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_page(self, wd):
        # Открывает страницу
        wd.get("https://localhost/addressbook/edit.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
