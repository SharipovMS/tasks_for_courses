from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="good", header="good", footer="good"))


def test_add_group_empty(app):
    app.group.create(Group(name="", header="", footer=""))
