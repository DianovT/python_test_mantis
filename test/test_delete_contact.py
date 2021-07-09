from model.contact import contact



def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new_form(contact(firstname="firstname"))
    old_contact = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contact) - 1  == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[0:1] = []
    assert old_contact == new_contact




