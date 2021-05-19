# -*- coding: utf-8 -*-
import pytest
from model.test_create_contact_class import class_for_test_create_contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application() #инициализация фикстуры
    request.addfinalizer(fixture.destroy) #как разрушается фикстура
    return fixture

def test_add_create_contact(app): #тестовый метод
    app.session.login()
    app.contact.create(class_for_test_create_contact(firstname="Marat", second_name="Sharipov", lastname="Sericbaevich", nickname="murena", company="quality-lab", address="Moscow",
                                                     mobile="+7 906 523 43 03", home="-", work="-", email="murenashark@mail.ru", fax="-", email2="-", homepage="-", email3="-", bday="15",
                                                     bmonth="January", byear="1994", address2="Kostroma", dom="50", notes="Russia"))
    app.session.logout()

def test_add_create_contact_empty(app): #тестовый метод
    app.session.login()
    app.contact.create(class_for_test_create_contact(firstname="", second_name="", lastname="", nickname="", company="", address="",
                                                     mobile="", home="", work="", email="", fax="", email2="", homepage="", email3="", bday="",
                                                     bmonth="-", byear="", address2="", dom="", notes=""))
    app.session.logout()