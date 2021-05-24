from model.test_create_contact_class import class_for_test_create_contact

def test_mod_contact(app): #тестовый метод
    app.session.login()
    app.contact.modify_first_contact(class_for_test_create_contact(firstname="Timur", second_name="Sharipov", lastname="Sericbaevich", nickname="murena", company="quality-lab", address="Moscow",
                                                     mobile="+7 906 523 43 03", home="-", work="-", email="murenashark@mail.ru", fax="-", email2="-", homepage="-", email3="-", bday="15",
                                                     bmonth="January", byear="1994", address2="Kostroma", dom="50", notes="Russia"))
    app.session.logout()