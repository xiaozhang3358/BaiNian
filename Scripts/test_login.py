import sys, os
sys.path.append(os.getcwd())
import allure
from Page.page_in import PageIn
import pytest
import time
from Base.read_yaml import ReadYAML


# 读取参数函数 封装
def get_data():
    #     自定义空列表
    arrs = []
    for data in ReadYAML('login_data.yaml').read_yaml().values():
        arrs.append((data.get('username'), data.get('pwd'), data.get('nick_text'), data.get('expect_toast')))

    return arrs


class TestLogin():
    @allure.step("开始初始化操作")
    def setup_class(self):
        allure.attach("步骤描述：","实例化入口类")
        self.page = PageIn()
        allure.attach("步骤描述：", "实例化Login入口类")
        self.login = self.page.page_get_login()
        # 点击我
        self.login.page_click_me()
        # 点击已有账号登录
        self.login.page_click_login_link()

    def teardown_class(self):
        self.login.driver.quit()

    @pytest.mark.parametrize('username,pwd,nick_text,expect_toast', get_data())
    def test_login(self, username, pwd, nick_text, expect_toast):
        if nick_text:
            # 输入用户名
            self.login.page_input_username(username)
            # 输入密码
            self.login.page_input_pwd(pwd)
            # 点击登录
            self.login.page_login_btn()
            # 获取昵称
            nickname = self.login.page_get_nickname()
            # 断言
            try:
                allure.attach("步骤描述：", "开始断言")
                assert nick_text in nickname

            except:
                # 截图
                self.login.base_get_screenshot()
                # 失败图片写入报告
                with open('./Image/faild.png', 'rb') as f:
                    allure.attach('失败请看图', f.read(), allure.attach_type.PNG)
                # 抛出异常
                raise
            finally:
                # 点击设置
                self.login.page_click_setting()
                # 滑动
                self.login.page_drag_and_drop()
                # 点击退出
                self.login.page_click_exit_btn()
                # 确认退出
                self.login.page_click_exit_ok_btn()
                # 下次再次登录
                # 点击我
                self.login.page_click_me()
                # 点击已有账号登录
                self.login.page_click_login_link()
        else:
            # 输入用户名
            self.login.page_input_username(username)
            # 输入密码
            self.login.page_input_pwd(pwd)
            # 点击登录
            self.login.page_login_btn()
            try:
                # 获取toast内容,断言
                toast = self.login.base_get_toast(expect_toast)
                assert expect_toast in toast
            except:
                # 截图
                self.login.base_get_screenshot()
                # 失败图片写入报告
                with open('./Image/faild.png', 'rb') as f:
                    allure.attach('失败请看图', f.read(), allure.attach_type.PNG)
                # 抛出异常
                raise

