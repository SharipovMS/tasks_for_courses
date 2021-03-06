import random
from model.contact import Contact
from time import sleep

#def test_delete_some_contact(app, db, check_ui): #тестовый метод
#    if app.contact.count() == 0:
#        app.contact.create((Contact(firstname="Marat")))
#    old_contacts = app.contact.get_contact_list()
#    index = randrange(len(old_contacts))
#    app.contact.delete_contact_by_index(index)
#    sleep(1)
#    assert len(old_contacts) - 1 == app.contact.count()
#    new_contacts = app.contact.get_contact_list()
#    old_contacts[index:index+1] = []
#    assert old_contacts == new_contacts

def test_delete_some_contact(app, db, check_ui): #тестовый метод
    app.contact.count()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    sleep(1)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    print(db.get_contact_list())
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)