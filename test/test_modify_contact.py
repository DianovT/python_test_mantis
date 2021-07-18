from model.contact import contact
from random import randrange




def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new_form(contact(firstname="test",lastname="test",bday="9"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    modify_contact = contact(firstname="firstname_test",
        middlename="middlename_test",
        lastname="lastname_test",
        nickname="nickname",
        company="company2",
        address="address2",
        home_number="43533534",
        mob_number="234242",
        work_number="75345345",
        EMail="test111@test,com",
        bday="5",
        bmonth="March",
        byear="1989")
    modify_contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, modify_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = modify_contact
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)



