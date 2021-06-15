from model.test_create_contact_class import class_for_test_create_contact
from random import randrange

def test_mod_contact(app): #тестовый метод
    if app.contact.count() == 0:
        app.contact.create((class_for_test_create_contact(firstname="Marat")))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = class_for_test_create_contact(firstname="Timur")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=class_for_test_create_contact.id_or_max) == sorted(new_contacts, key=class_for_test_create_contact.id_or_max)