from model.group import Group

def test_mod_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.mod_first_group(Group(name="bad_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_mod_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.mod_first_group(Group(header="bad_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)