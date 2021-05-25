from model.group import Group

def test_mod_first_group_name(app):
    app.group.mod_first_group(Group(name="bad_name"))

def test_mod_first_group_header(app):
    app.group.mod_first_group(Group(header="bad_header"))
