class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, login="admin", password="secret"):
        # Авторизация
        wd = self.app.wd
        self.app.open_page() #вынесен в функцию чтобы страница открывалась в авторизации.
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")
