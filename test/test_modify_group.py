from model.group import Group
from random import randrange
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join ([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdate = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 6), header=random_string("header", 10), footer=random_string("footer", 15))
    for i in range(3)
]

@pytest.mark.parametrize("group", testdate, ids=[repr(x) for x in testdate])
def test_edit_group_name(app, group):
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    groups = group
    groups.id = old_groups[index].id
    app.group.modify_group_by_index(index, groups)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = groups
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_group_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="edit_test"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


