from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from pages.contact_page import ContactPage
from pages.main_page import Opentions


class AddMemberPage(BasePage):
    def add_member(self):

        self.driver.find_element(By.ID,"username").send_keys("皮城女警")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("333")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("15810986271")
        return self
    def save_member(self):
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save" ).click()
        return ContactPage(self.driver)

    def cancel_member(self):
     pass