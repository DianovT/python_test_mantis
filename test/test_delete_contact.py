from model.contact import contact



def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new_form(contact(firstname="firstname"))
    app.contact.delete_first_contact()
