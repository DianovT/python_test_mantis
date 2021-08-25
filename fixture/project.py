from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_page_manage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()

    def select_manage_projects(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, Project):
        wd = self.app.wd
        self.change_field("name", Project.view_status)
        self.change_field("status", Project.status)
        self.change_field("view_state", Project.view_status)
        self.change_field("description", Project.description)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name in ('status', 'view_state'):
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            else:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

    def create(self, project):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_page_manage()
        self.select_manage_projects()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input.button").click()
        self.project_cash = None

    def delete_project_by_name(self, project):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_page_manage()
        self.select_manage_projects()
        wd.find_element_by_xpath("//a[contains(text(),'" + project + "')]").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_css_selector("input.button").click()
        self.project_cash = None

    progect_cash = None

    def get_project_list(self):
        if self.project_cash is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.open_page_manage()
            self.select_manage_projects()
            self.project_cash = []
            for element in (wd.find_elements_by_xpath("/html/body/table[3]/tbody/tr")):
                if element.get_attribute("class") not in ('', 'row-category'):
                    cells = element.find_elements_by_tag_name("td")
                    project_name = cells[0].text
                    self.project_cash.append(Project(project_name=project_name))
        return list(filter(None, self.project_cash))