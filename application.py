from selenium.webdriver.android import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

class Application:
    def __init__(self): #Запуск браузера
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_page_add_new(self):
        # Открывает страницу
        wd = self.wd
        wd.get("https://localhost/addressbook/edit.php")

    def login(self, login="admin", password="secret"):
        # Авторизация
        wd = self.wd
        self.open_page_add_new() #вынесен в функцию чтобы страница открывалась в авторизации.
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_contact(self, test_create_contact_class):
        # Заполнение формы адресной книги
        wd = self.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(test_create_contact_class.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(test_create_contact_class.second_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(test_create_contact_class.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(test_create_contact_class.nickname)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(test_create_contact_class.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(test_create_contact_class.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(test_create_contact_class.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(test_create_contact_class.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(test_create_contact_class.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(test_create_contact_class.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(test_create_contact_class.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(test_create_contact_class.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(test_create_contact_class.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(test_create_contact_class.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(test_create_contact_class.bday)
        #wd.find_element_by_xpath("//option[@value='15']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(test_create_contact_class.bmonth)
        #wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(test_create_contact_class.byear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(test_create_contact_class.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(test_create_contact_class.dom)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(test_create_contact_class.notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()