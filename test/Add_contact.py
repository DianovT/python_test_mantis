# -*- coding: utf-8 -*-
from model.contact import contact


    
def test_add_contact(app):
        app.contact.fill_new_form(contact(
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
            byear="1988"))

