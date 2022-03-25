
import time
from common.base import BaseApp
from pages.Always_allow import Power
from common.start import start_app
'''登录页面元素抓取'''

class Register(BaseApp):
    ''' 注册页面'''
    loc1 = {"name": "输入手机号", "by": "id", "value": "com.mmc.fengshui.pass:id/linghit_login_phone_number_et"}
    loc2 = {"name": "输入验证码", "by": "id", "value": "com.mmc.fengshui.pass:id/linghit_login_virfy_number_et"}
    loc3 = {"name": "输入密码", "by": "id", "value": "com.mmc.fengshui.pass:id/linghit_login_password_et"}
    loc4 = {"name": "点击地区", "by": "id", "value": "com.mmc.fengshui.pass:id/linghit_login_phone_number_area_btn"}
    loc5 = {"name": "点击选择中国大陆", "by": "text", "value": "中国大陆 +86"}
    loc6 = {"name": "点击确认注册", "by": "id", "value": "com.mmc.fengshui.pass:id/linghit_login_confirm_btn"}
    loc7 = {"name": "点击勾选用户协议", "by": "id", "value": "com.mmc.fengshui.pass:id/linghit_login_accept_ck"}


    def step_01(self):
        '''点击地区'''
        time.sleep(2)
        self.click(self.loc4)
        time.sleep(1)
        self.click(self.loc5)
        time.sleep(1)

    def step_02(self):
        '''未勾选点击确认注册'''
        time.sleep(2)
        self.click(self.loc6)
        time.sleep(1)
        self.is_toast_exist("请认真阅读并同意隐私协议")

    def step_03(self):
        '''已勾选点击确认注册'''
        time.sleep(2)
        self.click(self.loc7)
        time.sleep(1)
        self.click(self.loc6)
        time.sleep(1)
        self.is_toast_exist("请输入手机号码")

    def step_04(self):
        '''输入错误手机号'''
        time.sleep(2)
        self.send_text(self.loc1, "1882")
        time.sleep(1)
        self.click(self.loc6)
        time.sleep(1)
        self.is_toast_exist("请输入正确的手机号码")
        time.sleep(1)
        self.clear(self.loc1)

    def step_05(self):
        '''输入正确手机号'''
        time.sleep(2)
        self.send_text(self.loc1, "18826426272")
        time.sleep(1)
        self.click(self.loc6)
        time.sleep(1)
        self.is_toast_exist("请输入验证码")
        time.sleep(1)
        self.clear(self.loc1)

    def step_06(self):
        '''输入正确手机号和错误验证码'''
        time.sleep(2)
        self.send_text(self.loc1, "18826426272")
        time.sleep(1)
        self.send_text(self.loc2, "188")
        self.click(self.loc6)
        time.sleep(1)
        self.is_toast_exist("请输入密码")
        time.sleep(1)
        self.clear(self.loc1)
        self.clear(self.loc2)

    def step_07(self):
        '''输入正确手机号和错误验证码和错误密码'''
        time.sleep(2)
        self.send_text(self.loc1, "18902305954")
        time.sleep(1)
        self.send_text(self.loc2, "188")
        time.sleep(1)
        self.send_text(self.loc3, "1882")
        time.sleep(1)
        self.click(self.loc6)
        time.sleep(0.5)
        self.is_toast_exist("密码必须是6–18位字母或者数字")
        time.sleep(1)
        self.clear(self.loc1)
        self.clear(self.loc2)
        self.clear(self.loc3)

    def step_08(self):
        '''输入正确手机号和错误验证码和错误密码'''
        time.sleep(2)
        self.send_text(self.loc1, "18902305954")
        time.sleep(1)
        self.send_text(self.loc2, "188")
        time.sleep(1)
        self.send_text(self.loc3, "123456")
        time.sleep(1)
        self.click(self.loc6)
        time.sleep(1)
        self.is_toast_exist("注册失败了，请稍候重试啦")
        time.sleep(1)
        self.clear(self.loc1)
        self.clear(self.loc2)
        self.clear(self.loc3)
        self.driver.back()