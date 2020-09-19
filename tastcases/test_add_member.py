from pages.main_page import MainPage


class TestAddMember:
    def test_add_member(self):
        self.main=MainPage()
        #1.从首页跳转到添加成员页面 2.添加成员
        
        self .main.go_to_add_member().add_member().save_member()

    def test_contatact_member(self):
        self.main = MainPage()
        #1.从首页跳转到通讯录页面 2.跳转到添加成员页面
        #3.添加成员
        self.main.go_to_contact().go_to_add_member().add_member()
