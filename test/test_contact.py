from model.contact import Contact
import re

def test_contact_db_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Marat", lastname="TESTovich"))
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_in_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for index in range(len(db.get_contact_list())):
        assert contact_from_home_page[index].firstname == contact_in_db[index].firstname
        assert contact_from_home_page[index].lastname == contact_in_db[index].lastname
        assert contact_from_home_page[index].address == contact_in_db[index].address
        assert contact_from_home_page[index].all_phones_from_home_page == merge_phones_like_on_home_page(contact_in_db[index])
        assert contact_from_home_page[index].all_emails_from_home_page == merge_emails_like_on_home_page(contact_in_db[index])


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.workphone, contact.mobilephone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     filter(lambda x: x is not None,
                            [contact.email, contact.email2, contact.email3])))