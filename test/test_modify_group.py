from model.group import Group





def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test" ))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="edit_test"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="edit_test"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

