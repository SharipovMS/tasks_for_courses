from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self): #Запуск браузера
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_page_add_new(self):
        # Открывает страницу
        wd = self.wd
        wd.get("https://localhost/addressbook/edit.php")

    def open_page(self):
        # Открывает страницу
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False