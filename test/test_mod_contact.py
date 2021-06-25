from model.contact import Contact
from random import randrange

def test_mod_contact(app, db, check_ui): #тестовый метод
    if len(db.get_contact_list()) == 0:
        app.contact.create((Contact(firstname="Marat", lastname="TESTovich")))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Tamerlan")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max())

#def test_mod_contact(app, db, check_ui): #тестовый метод
#    if app.contact.count() == 0:
#        app.contact.create((Contact(firstname="Marat")))
#    old_contacts = app.contact.get_contact_list()
#    index = randrange(len(old_contacts))
#    contact = Contact(firstname="Timur")
#    contact.id = old_contacts[index].id
#    app.contact.modify_contact_by_index(index, contact)
#    assert len(old_contacts) == app.contact.count()
#    new_contacts = app.contact.get_contact_list()
#    old_contacts[index] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)