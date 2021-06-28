from model.contact import contact




def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(contact(
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
    app.session.logout()