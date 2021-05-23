from model.test_create_contact_class import class_for_test_create_contact

def test_mod_contact(app): #тестовый метод
    app.session.login()
    app.contact.modify_first_contact(class_for_test_create_contact(firstname="Timur", second_name="", lastname="", nickname="", company="", address="",
                                                                   mobile="", home="", work="", email="", fax="", email2="", homepage="", email3="", bday="",
                                                                   bmonth="-", byear="", address2="", dom="", notes=""))
    app.session.logout()