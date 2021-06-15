from model.test_create_contact_class import class_for_test_create_contact
from random import randrange

def test_delete_some_contact(app): #тестовый метод
    if app.contact.count() == 0:
        app.contact.create((class_for_test_create_contact(firstname="Marat")))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts