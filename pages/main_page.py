from selenium.webdriver.common.by import By

from pages.add_member_page import AddMemberPage
from pages.basepage import BasePage
from pages.contact_page import ContactPage
from selenium import webdriver


class Opentions(object):
    pass


class MainPage(BasePage):

    def go_to_contact(self):
        #对contactpage类进行实例化，表示业务逻辑的转换关系



        return ContactPage(self.driver)

    def go_to_add_member(self):


        self.driver.find_element(By.CSS_SELECTOR, "[node-type='addmember']").click()

        return AddMemberPage(self.driver)
