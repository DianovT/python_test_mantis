# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="test", header="test", footer="test"))
        self.logout()

    def test_add_empty_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook")
        return wd

    def login(self, username, password):
        wd = self.wd
        wd = self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, Group):
        wd = self.wd
        self.open_groups()
        # init_groups_creation
        wd.find_element_by_name("new").click()
        #fill_group_form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.footer)
        #submit_group_creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self,):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
