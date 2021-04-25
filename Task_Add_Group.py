# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TaskAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_task_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        # Отркытие страницы с группами
        self.open_group_page(wd)
        self.filling_form_group(wd)
        #закончили заполнение
        wd.find_element_by_link_text("group page").click()
        #Разлогинились
        self.logout(wd)
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def filling_form_group(self, wd):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        # заполнение формы
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("family")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("family")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("family")
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd):
        # Логаемся
        wd.find_element_by_name("user").click()
        wd.find_element_by_xpath("//input[@name='user']").clear()
        wd.find_element_by_xpath("//input[@name='user']").send_keys("admin")
        wd.find_element_by_xpath("//input[@name='pass']").clear()
        wd.find_element_by_xpath("//input[@name='pass']").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # открытие главной страницы
        wd.get("http://localhost/addressbook/group.php")

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
