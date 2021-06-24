from model.group import Group





def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="edit_test",header="edit_test", footer="edit_test"))
    app.session.logout()