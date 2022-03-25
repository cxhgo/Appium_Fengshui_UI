# -*- encoding:utf-8 -*-
import time
from common.base import BaseApp
'''登录页面元素抓取'''


class LoginPage(BaseApp):
    ''' 登录页面'''
    loc1 = {"name": "点击立即开启", "by": "text", "value": "立即开启"}
    loc2 = {"name": "点击登录/注册", "by": "text", "value": "登录/注册"}
    loc3 = {"name": "点击确定", "by": "text", "value": "始终允许"}
    loc4 = {"name": "点击其他号码登录", "by": "text", "value": "其他号码登录"}
    loc5 = {"name": "点击密码登录", "by": "text", "value": "密码登录"}
    loc6 = {"name": "输入手机号", "by": "id", "value": "com.mmc.feelsowarm:id/code_login_phone"}
    loc7 = {"name": "输入密码", "by": "id", "value": "com.mmc.feelsowarm:id/login_phone_password"}
    loc9 = {"name": "点击登录", "by": "text", "value": "登录"}
    loc10 = {"name": "点击始终允许", "by": "text", "value": "始终允许"}

    def step_01(self):
        '''向左滑动'''
        time.sleep(2)
        self.swipe_left()
        self.swipe_left()

    def step_02(self):

        '''立即开启'''
        time.sleep(2)
        self.click(self.loc1)
        try:
            self.driver.find_element_by_xpath("//*[@text='允许']").click()
        except:
            pass

    def step_03(self):
        '''点击登录/注册'''
        self.click(self.loc2)
        try:
            self.driver.find_element_by_xpath("//*[@text='始终允许']").click()
            self.driver.find_element_by_xpath("//*[@text='始终允许']").click()
            self.driver.find_element_by_xpath("//*[@text='始终允许']").click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath("//*[@text='其他号码登录']").click()
        except:
            pass

    def step_04(self):
        '''点击密码登录'''
        self.click(self.loc5)
        try:
            self.driver.find_element_by_xpath("//*[@text='始终允许']").click()
            self.driver.find_element_by_xpath("//*[@text='始终允许']").click()
        except:
            pass

    def step_05(self):
        '''输入手机号'''
        self.send_text(self.loc6, "18819447984")

    def step_06(self):
        '''输入密码'''
        self.send_text(self.loc7, "123456")

    def step_07(self):
        '''点击登录'''
        self.click(self.loc9)

    def step_08(self):
        '''点击同意'''
        try:
            self.driver.find_element_by_xpath("//*[@text='允许']").click()
            self.driver.find_element_by_xpath("//*[@text='允许']").click()
            self.driver.find_element_by_xpath("//*[@text='允许']").click()
            self.driver.find_element_by_xpath("//*[@text='允许']").click()
            self.driver.find_element_by_xpath("//*[@text='允许']").click()
            self.driver.find_element_by_xpath("//*[@text='允许']").click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath("//*[@text='允许']").click()
        except:
            pass
            pass
        try:
            self.driver.find_element_by_xpath("//*[@text='始终允许']").click()
            self.driver.find_element_by_xpath("//*[@text='始终允许']").click()
            self.driver.find_element_by_xpath("//*[@text='始终允许']").click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath("//*[@text='同意']").click()
        except:
            pass







