from model.contact import contact




def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new_form(contact(firstname="test",lastname="test",bday="9"))
    old_contact = app.contact.get_contact_list()
    contacts = contact(firstname="firstname",
        middlename="middlename",
        lastname="lastname",
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
    app.contact.modify_first_contact(contacts)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contacts
    assert sorted(old_contact, key=contact.id_or_max) == sorted(new_contact, key=contact.id_or_max)



