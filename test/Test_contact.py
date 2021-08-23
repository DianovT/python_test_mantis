from model.contact import Contact


import re

def test_contact_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contact_from_home_page) == len(contact_from_db)
    for i in range(len(contact_from_home_page)):
        assert contact_from_home_page[i].id == contact_from_db[i].id
        assert contact_from_home_page[i].firstname == contact_from_db[i].firstname
        assert contact_from_home_page[i].lastname == contact_from_db[i].lastname
        assert contact_from_home_page[i].address == contact_from_db[i].address
        assert contact_from_home_page[i].all_EMail_from_homepage == merge_email_like_on_home_page(contact_from_db[i])
        assert contact_from_home_page[i].all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_db[i])

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                                                [contact.home_phone, contact.mob_phone,
                                                                 contact.work_phone, contact.second_phone]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", [contact.EMail, contact.EMail2, contact.EMail3]))
