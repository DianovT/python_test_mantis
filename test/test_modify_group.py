from model.group import Group





def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test" ))
    app.group.modify_first_group(Group(name="edit_test"))

def test_edit_group_header(app):
    app.group.modify_first_group(Group(header="edit_test"))
