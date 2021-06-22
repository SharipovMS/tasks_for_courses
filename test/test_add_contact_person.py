# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_create_contact(app, json_contacts): #тестовый метод
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
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