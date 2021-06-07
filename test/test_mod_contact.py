from model.test_create_contact_class import class_for_test_create_contact

def test_mod_contact(app): #тестовый метод
    if app.contact.count() == 0:
        app.contact.create((class_for_test_create_contact(firstname="Marat")))
    old_contacts = app.contact.get_contact_list()
    contact = class_for_test_create_contact(firstname="Timur")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=class_for_test_create_contact.id_or_max) == sorted(new_contacts, key=class_for_test_create_contact.id_or_max)