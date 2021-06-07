# -*- coding: utf-8 -*-
from model.test_create_contact_class import class_for_test_create_contact

def test_add_create_contact(app): #тестовый метод
    old_contacts = app.contact.get_contact_list()
    contact = class_for_test_create_contact(firstname="Marat", second_name="Sharipov", lastname="Sericbaevich",
                                                     nickname="murena", company="quality-lab", address="Moscow",
                                                     mobile="+7 906 523 43 03", email="murenashark@mail.ru", bday="16",
                                                     bmonth="January", byear="1994", address2="Kostroma", notes="Russia")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=class_for_test_create_contact.id_or_max) == sorted(new_contacts,
                                                                                       key=class_for_test_create_contact.id_or_max)

def test_add_create_contact_empty(app): #тестовый метод
    old_contacts = app.contact.get_contact_list()
    contact = class_for_test_create_contact()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=class_for_test_create_contact.id_or_max) == sorted(new_contacts, key=class_for_test_create_contact.id_or_max)