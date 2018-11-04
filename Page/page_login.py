import allure

import Page
from Base.base import Base


class PageLogin(Base):
    # 点击我
    @allure.step("点击我")
    def page_click_me(self):
        self.base_click_element(Page.login_me)

    # 点击以有帐号，去登录
    @allure.step("点击以有帐号，去登录")
    def page_click_login_link(self):
        self.base_click_element(Page.login_name_ok_link)

    # 输入用户名
    @allure.step("输入用户名")
    def page_input_username(self, username):
        self.base_input(Page.login_username, username)

    # 输入密码
    @allure.step("输入密码")
    def page_input_pwd(self, pwd):
        self.base_input(Page.login_password, pwd)

    # 点击登录
    @allure.step("点击登录")
    def page_login_btn(self):
        self.base_click_element(Page.login_btn)

    # 获取昵称断言
    def page_get_nickname(self):
        return self.base_get_text(Page.login_nickname)

    #  点击设置
    @allure.step("点击设置")
    def page_click_setting(self):
        self.base_click_element(Page.login_setting)

    # 滑动 从消息推送到修改密码
    @allure.step("滑动，从消息推送-->修改密码")
    def page_drag_and_drop(self):
        el1 = self.base_find_element(Page.login_msg_send)
        el2 = self.base_find_element(Page.login_modify_pwd)
        self.base_drag_and_drop(el1, el2)

    # 点击退出按钮
    @allure.step("点击退出按钮")
    def page_click_exit_btn(self):
        self.base_click_element(Page.login_logout)

    # 确认退出
    @allure.step("确认退出")
    def page_click_exit_ok_btn(self):
        self.base_click_element(Page.login_logout_ok)
