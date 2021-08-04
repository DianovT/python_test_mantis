from model.group import Group
from random import randrange
import random

def test_edit_group_name(app, db, check_ui, json_groups):
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    choice_group = random.choice(old_groups)
    index = old_groups.index(choice_group)
    modify_group = group
    app.group.modify_group_by_id(choice_group.id, modify_group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = modify_group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_edit_group_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="edit_test"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)



