# -*- coding: utf-8 -*-
from model.contact import Contact

testdata = [
    Contact(firstname="firstname1", second_name="second_name1", lastname="lastname1",
                      nickname="nickname1", company="company1", address="address1",
                      mobile="mobile1", email="email1", bday="16",
                      bmonth="January", byear="1994", address2="address2", notes="notes1"),
    Contact(firstname="firstname2", second_name="second_name2", lastname="lastname3",
                      nickname="nickname2", company="company2", address="address2",
                      mobile="mobile2", email="email2", bday="26",
                      bmonth="January", byear="1996", address2="address3", notes="notes3")
]
