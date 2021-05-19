from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self): #Запуск браузера
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_page_add_new(self):
        # Открывает страницу
        wd = self.wd
        wd.get("https://localhost/addressbook/edit.php")

    def destroy(self):
        self.wd.quit()