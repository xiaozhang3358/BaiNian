from Base.get_driver import get_driver
from Page.page_address import PageAddress
from Page.page_login import PageLogin


class PageIn():
    def __init__(self):
        self.driver = get_driver()

    # 获取登录页面的对象
    def page_get_login(self):
        return PageLogin(self.driver)

    # 获取地址页面的对象
    def page_get_address(self):
        return PageAddress(self.driver)
