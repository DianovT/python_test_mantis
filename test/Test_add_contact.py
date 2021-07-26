# -*- coding: utf-8 -*-
from model.contact import Сontact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(prefix, maxlen):
    symbols = string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdate = [Сontact(firstname="", middlename="", lastname="")] + [
    Сontact(
            firstname=random_string("firstname", 6),
            middlename=random_string("middlename", 8),
            lastname=random_string("lastname", 10),
            company=random_string("company", 6),
            address=random_string("address", 6),
            home_phone=random_number("7926", 7),
            mob_phone=random_number("+7926", 7),
            work_phone=random_number("8926", 7),
            second_phone=random_number("926", 7),
            EMail=random_string("EMail", 6),
            bday="4",
            bmonth="March",
            byear=random_number("19", 2))
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdate, ids=[repr(x) for x in testdate])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.fill_new_form(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Сontact.id_or_max) == sorted(new_contacts, key=Сontact.id_or_max)
