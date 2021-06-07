from sys import maxsize

class class_for_test_create_contact:

    def __init__(self, firstname=None, second_name=None, lastname=None, nickname=None, company=None, address=None, mobile=None, home=None, work=None,
                           email=None, fax=None, email2=None, homepage=None, email3=None, bday=None, bmonth=None, byear=None, address2=None, dom=None, notes=None, id=None, name=None):
        self.firstname = firstname
        self.second_name = second_name
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.mobile = mobile
        self.home = home
        self.work = work
        self.email = email
        self.fax = fax
        self.email2 = email2
        self.homepage = homepage
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.dom = dom
        self.notes = notes
        self.name = name
        self.id = id


    def __repr__(self):
        return "%s:s%" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize