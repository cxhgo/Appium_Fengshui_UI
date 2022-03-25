
import time
from common.base import BaseApp
from pages.Always_allow import Power
from common.start import start_app
'''登录页面元素抓取'''

class LoginPage(BaseApp):
    ''' 登录页面'''
    loc1 = {"name": "点击课程tab", "by": "id", "value": "com.mmc.fengshui.pass:id/vBCNavigationTab5"}
    loc2 = {"name": "点击头像", "by": "id", "value": "com.mmc.fengshui.pass:id/ivUserAvatar"}
    loc3 = {"name": "点击本机号码登录", "by": "text", "value": "本机号码一键登录"}
    loc4 = {"name": "点击其他方式登录", "by": "text", "value": "其他方式登录"}
    loc5 = {"name": "点击隐私政策", "by": "text", "value": "《隐私政策》"}
    loc6 = {"name": "点击服务协议", "by": "text", "value": "《服务协议》"}
    loc7 = {"name": "点击密码登录", "by": "text", "value": "账号密码登录"}
    loc8 = {"name": "账号输入", "by": "id", "value": "com.mmc.fengshui.pass:id/linghit_login_phone_number_et"}
    loc9 = {"name": "输入密码", "by": "id", "value": "com.mmc.fengshui.pass:id/linghit_login_password_et"}
    loc10 = {"name": "点击登录", "by": "text", "value": "登录"}
    loc11 = {"name": "点击勾选用户协议", "by": "id", "value": "com.mmc.fengshui.pass:id/linghit_quick_checkbox"}
    loc12 = {"name": "点击注册", "by": "text", "value": "注册"}
    loc13 = {"name": "点击忘记密码?", "by": "text", "value": "忘记密码?"}
    loc14 = {"name": "点击手机号找回密码", "by": "text", "value": "手机号找回密码"}

    def step_01(self):
        '''点击导航栏课程tab'''
        time.sleep(2)
        self.click(self.loc1)
        time.sleep(1)

    def step_02(self):
        '''点击头像进入登录界面'''
        time.sleep(2)
        self.click(self.loc2)
        time.sleep(1)

    def step_03(self):
        self.is_toast_exist("请同意《服务协议》和《隐私政策》")

    def step_04(self):
        '''点击本机号码一键登录'''
        time.sleep(2)
        self.click(self.loc3)
        time.sleep(1)
        self.is_toast_exist("请同意《服务协议》和《隐私政策》")

    def step_05(self):
        '''点击服务协议'''
        time.sleep(2)
        self.click(self.loc6)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    def step_06(self):
        '''点击隐私政策'''
        time.sleep(2)
        self.click(self.loc5)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    def step_07(self):
        '''点击其他方式登录'''
        time.sleep(2)
        self.click(self.loc4)

    def step_08(self):
        '''切换账号密码方式登录'''
        time.sleep(2)
        self.click(self.loc7)

    def step_09(self):
        '''未勾选协议点击同意'''
        time.sleep(2)
        self.click(self.loc10)
        self.is_toast_exist("请同意《服务协议》和《隐私政策》")

    def step_10(self):
        '''勾选隐私协议和用户协议'''
        time.sleep(2)
        self.click(self.loc11)
        time.sleep(2)

    def step_11(self):
        '''未输入账号密码点击同意'''
        time.sleep(2)
        LoginPage.step_10(self)
        self.click(self.loc10)
        self.is_toast_exist("请输入账号或邮箱")
        LoginPage.step_10(self)

    def step_12(self):
        '''未输入密码点击同意'''
        time.sleep(2)
        LoginPage.step_10(self)
        self.send_text(self.loc8, "18826426272")
        self.click(self.loc10)
        self.is_toast_exist("请输入密码")
        self.clear(self.loc8)
        LoginPage.step_10(self)

    def step_13(self):
        '''输入错误账号和密码点击同意'''
        time.sleep(2)
        LoginPage.step_10(self)
        self.send_text(self.loc8, "124")
        self.send_text(self.loc9, "123456")
        self.click(self.loc10)
        self.is_toast_exist("帐号不存在")
        self.clear(self.loc8)
        self.clear(self.loc9)
        LoginPage.step_10(self)

    def step_14(self):
        '''输入错误密码点击同意'''
        time.sleep(2)
        LoginPage.step_10(self)
        self.send_text(self.loc8, "18902305954")
        self.send_text(self.loc9, "1234")
        self.click(self.loc10)#loc10
        self.is_toast_exist("密码错误")
        self.clear(self.loc8)
        self.clear(self.loc9)
        LoginPage.step_10(self)


    def step_15(self):
        '''点击注册'''
        time.sleep(2)
        self.click(self.loc12)

    def step_16(self):
        '''点击忘记密码'''
        time.sleep(2)
        self.click(self.loc13)
        time.sleep(2)
        self.click(self.loc14)


    def step_17(self):
        '''点击登录'''
        time.sleep(2)
        self.click(self.loc10)


    def step_18(self):
        '''输入账号密码登录'''
        time.sleep(2)
        self.send_text(self.loc8, "18826426272")
        self.send_text(self.loc9, "123456")
        LoginPage.step_17(self)


