from model.contact import contact




def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new_form(contact(firstname="test",lastname="test",bday="9"))
    app.contact.modify_first_contact(contact(
        firstname="firstname",
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
        byear="1989"))
