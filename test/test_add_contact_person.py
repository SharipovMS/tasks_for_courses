# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=random_string("firstname",20), second_name=random_string("second_name",20), lastname=random_string("lastname",20),
                      nickname=random_string("nickname",20), company=random_string("company",20), address=random_string("address",20),
                      mobile=random_string("mobile",20), email=random_email("email",20), bday="16",
                      bmonth="January", byear="1994", address2=random_string("address2",20), notes=random_string("notes",20))
    for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_create_contact(app, contact): #тестовый метод
    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="Marat", second_name="Sharipov", lastname="Sericbaevich",
#                      nickname="murena", company="quality-lab", address="Moscow",
#                      mobile="+7 906 523 43 03", email="murenashark@mail.ru", bday="16",
#                      bmonth="January", byear="1994", address2="Kostroma", notes="Russia")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_add_create_contact_empty(app): #тестовый метод
#    old_contacts = app.contact.get_contact_list()
#    contact = class_for_test_create_contact()
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=class_for_test_create_contact.id_or_max) == sorted(new_contacts, key=class_for_test_create_contact.id_or_max)