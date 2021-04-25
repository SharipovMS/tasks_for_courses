# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        #Открывает страницу
        wd.get("https://localhost/addressbook/edit.php")
        #Авторизация
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        #Заполнение формы адресной книги
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Marat")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Sharipov")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Sericbaevich")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("murena")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("quality-lab")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Moscow")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("-")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("+7 906 523 43 03")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("-")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("-")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("murenashark@mail.ru")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("-")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("-")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("-")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("15")
        wd.find_element_by_xpath("//option[@value='15']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1994")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Kostroma")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("50")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("Russia")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("Logout").click()

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
