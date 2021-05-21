from model.group import Group

def test_add_group(app):
    app.session.login()
    app.group.create(Group(name="good", header="good", footer="good"))
    app.session.logout()

def test_add_group_empty(app):
    app.session.login()
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()