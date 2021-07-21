from model.contact import Сontact


import re

def test_contact_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == clear(contact_from_edit_page.lastname)
    assert contact_from_home_page.firstname == clear(contact_from_edit_page.firstname)
    assert contact_from_home_page.address == clear(contact_from_edit_page.address)
    assert contact_from_home_page.all_EMail_from_homepage == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                                                [contact.home_phone, contact.mob_phone,
                                                                 contact.work_phone, contact.second_phone]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                                            [contact.EMail, contact.EMail2, contact.EMail3]))))
