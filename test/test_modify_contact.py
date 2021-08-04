from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    if len(db.get_contact_list()) == 0:
        app.contact.fill_new_form(contact)
    old_contacts = db.get_contact_list()
    choice_contact = random.choice(old_contacts)
    index = old_contacts.index(choice_contact)
    modify_contact = contact
    app.contact.modify_contact_by_id(choice_contact.id, modify_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = modify_contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),key=Contact.id_or_max)



