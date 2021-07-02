from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Marat", lastname="TESTovich"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="TEST"))
    if len(db.get_contacts_not_in_group()) == 0:
        app.contact.create(Contact(firstname="Marat", lastname="TESTovich"))
    group = app.group.get_group_list()
    groups = random.choice(group)
    group_id = groups.id
    contacts = db.get_contacts_not_in_group()
    contact = random.choice(contacts)
    contact_id = contact.id
    old_contact = db.get_contacts_in_group()
    app.contact.add_contact_to_group(contact_id, group_id)
    new_contacts = db.get_contacts_in_group()
    assert len(old_contact) + 1 == len(new_contacts)
    contact_ui = db.get_contacts_in_group()
    if check_ui:
        assert sorted(contact_ui, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)