from pages.basepage import BasePage


class ContactPage(BasePage):

    def go_to_add_member(self):
        #解决循环导入问题
        from pages.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)