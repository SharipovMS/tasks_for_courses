from model.test_create_contact_class import class_for_test_create_contact

def test_delete_contact(app): #тестовый метод

    if app.contact.count() == 0:
        app.contact.create((class_for_test_create_contact(firstname="Marat")))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts