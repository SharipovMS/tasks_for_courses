# -*- coding: utf-8 -*-
from model.test_create_contact_class import class_for_test_create_contact

def test_add_create_contact(app): #тестовый метод
    app.contact.create(class_for_test_create_contact(firstname="Marat", second_name="Sharipov", lastname="Sericbaevich", nickname="murena", company="quality-lab", address="Moscow",
                                                     mobile="+7 906 523 43 03", home="-", work="-", email="murenashark@mail.ru", fax="-", email2="-", homepage="-", email3="-", bday="15",
                                                     bmonth="January", byear="1994", address2="Kostroma", dom="50", notes="Russia"))


def test_add_create_contact_empty(app): #тестовый метод
    app.contact.create(class_for_test_create_contact(firstname="", second_name="", lastname="", nickname="", company="", address="",
                                                     mobile="", home="", work="", email="", fax="", email2="", homepage="", email3="", bday="",
                                                     bmonth="-", byear="", address2="", dom="", notes=""))
