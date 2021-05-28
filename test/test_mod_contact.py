from model.test_create_contact_class import class_for_test_create_contact

def test_mod_contact(app): #тестовый метод
    if app.contact.count() == 0:
        app.contact.create((class_for_test_create_contact(firstname="Marat")))
    app.contact.modify_first_contact(class_for_test_create_contact(firstname="Timur"))
