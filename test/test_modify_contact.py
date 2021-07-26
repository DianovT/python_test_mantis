from model.contact import Сontact
from random import randrange



def test_modify_some_contact(app, data_contacts):
    contact = data_contacts
    if app.contact.count() == 0:
        app.contact.fill_new_form(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    modify_contact = contact
    modify_contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, modify_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = modify_contact
    assert sorted(old_contacts, key=Сontact.id_or_max) == sorted(new_contacts, key=Сontact.id_or_max)



