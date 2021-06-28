


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, Group):
        wd = self.app.wd
        self.open_groups()
        # init_groups_creation
        wd.find_element_by_name("new").click()
        #fill_group_form
        self.fill_group_form(Group)
        #submit_group_creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_group_form(self, Group):
        wd = self.app.wd
        self.change_field_value("group_name", Group.name)
        self.change_field_value("group_header", Group.header)
        self.change_field_value("group_footer", Group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups()
        #select first group
        self.select_first_group()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def edit_first_group(self, new_group_date):
        wd = self.app.wd
        self.open_groups()
        #select first group
        self.select_first_group()
        #submit edit
        wd.find_element_by_name("edit").click()
        #fill_edit_group_form
        self.fill_group_form(new_group_date)
        #submit_group_creation
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()