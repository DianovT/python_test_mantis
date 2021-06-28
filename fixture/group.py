


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
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def edit_group(self, Group):
        wd = self.app.wd
        self.open_groups()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #submit edit
        wd.find_element_by_name("edit").click()
        #fill_edit_group_form
        self.fill_group_form(Group)
        #submit_group_creation
        wd.find_element_by_name("update").click()
        self.return_to_group_page()


    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()