def test_delete_contact(app): #тестовый метод
    app.session.login()
    app.contact.delete()
    app.session.logout()