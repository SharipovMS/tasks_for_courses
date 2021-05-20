import pytest
from fixture.application import Application
from model.group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.input_login(username="admin", password="secret")
    app.click_login()
    app.create_group(Group(name="good", header="good", footer="good"))
    app.logout()

def test_add_group_empty(app):
    app.input_login(username="admin", password="secret")
    app.click_login()
    app.create_group(Group(name="", header="", footer=""))
    app.logout()