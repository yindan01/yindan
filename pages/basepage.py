from selenium.webdriver.chrome import webdriver

from pages.main_page import Opentions


class BasePage:
    def __init__(self,driver_base=None):
        #避免driver的重复实例化

        if driver_base is None:
           option = Opentions()
           option.debugger_address = '127.0.0.1:9222'
           self.driver = webdriver.Chrome(options=option)

           self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        else:
            self.driver=driver_base
            self.driver.implicitly_wait(3)