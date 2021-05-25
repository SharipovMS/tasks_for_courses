from model.group import Group

def test_mod_first_group_name(app):
    app.session.login()
    app.group.mod_first_group(Group(name="bad_name"))
    app.session.logout()

def test_mod_first_group_header(app):
    app.session.login()
    app.group.mod_first_group(Group(header="bad_header"))
    app.session.logout()