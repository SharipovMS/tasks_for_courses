from model.group import Group

def test_mod_first_group(app):
    app.session.login()
    app.group.mod_first_group(Group(name="bad", header="bad", footer="bad"))
    app.session.logout()