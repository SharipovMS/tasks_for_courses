from selenium.webdriver.support.select import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        # открытие главной страницы
        wd = self.app.wd
        wd.get("https://localhost/addressbook/")

    def open_cont_page(self):
        # открытие главной страницы
        wd = self.app.wd
        wd.get("https://localhost/addressbook/edit.php")

    def create(self, test_create_contact_class):
        # Заполнение формы адресной книги
        wd = self.app.wd
        self.open_cont_page()
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

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, test_create_contact_class):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//img[@alt='Edit'])[1]").click()
        self.create(test_create_contact_class)
