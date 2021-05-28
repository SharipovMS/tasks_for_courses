from model.group import Group

def test_mod_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.mod_first_group(Group(name="bad_name"))

def test_mod_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.mod_first_group(Group(header="bad_header"))
