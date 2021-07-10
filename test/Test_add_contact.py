# -*- coding: utf-8 -*-
from model.contact import contact


    
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contacts = contact(
            firstname="name1",

            middlename="name2",
            lastname="name3",
            nickname="testname",
            company="company",
            address="address",
            home_number="9377722",
            mob_number="23455552525",
            work_number="2131231",
            EMail="test@test,com",
            bday="4",
            bmonth="March",
            byear="1988")
    app.contact.fill_new_form(contacts)
    assert len(old_contacts) + 1  == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)

