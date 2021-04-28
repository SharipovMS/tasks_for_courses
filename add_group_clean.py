# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
import unittest, time, re


class AddGroupClean(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group_clean(self):
        wd = self.wd
        self.open_home_page(wd)
        self.input_login(wd, username="admin", password="secret")
        self.click_login(wd)
        self.open_page_group(wd)
        self.create_group(wd, Group(name="good", header="good", footer="good"))
        self.check_page_group(wd)
        self.logout(wd)

    def test_add_group_empty(self):
        wd = self.wd
        self.open_home_page(wd)
        self.input_login(wd, username="admin", password="secret")
        self.click_login(wd)
        self.open_page_group(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        self.check_page_group(wd)
        self.logout(wd)

    def logout(self, wd):
        # Выход
        wd.find_element_by_link_text("Logout").click()

    def check_page_group(self, wd):
        # Проверка страницы группы
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, group):
        # Ввод данных в форму
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()

    def open_page_group(self, wd):
        # Открытие страницы группы
        wd.find_element_by_link_text("groups").click()

    def click_login(self, wd):
        # Вход
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def input_login(self, wd, username, password):
        # ввод логин/пароля
        wd.find_element_by_name("user").click()
        wd.find_element_by_xpath("//input[@name='user']").clear()
        wd.find_element_by_xpath("//input[@name='user']").send_keys(username)
        wd.find_element_by_xpath("//input[@name='pass']").clear()
        wd.find_element_by_xpath("//input[@name='pass']").send_keys(password)

    def open_home_page(self, wd):
        # открытие главной страницы
        wd.get("https://localhost/addressbook/")

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