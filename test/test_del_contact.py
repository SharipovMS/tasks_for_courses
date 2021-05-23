def test_delete_contact(app): #тестовый метод
    app.session.login()
    app.contact.delete_first_contact()
    app.session.logout()