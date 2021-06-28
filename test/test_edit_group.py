from model.group import Group





def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="edit_test"))

def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="edit_test"))
