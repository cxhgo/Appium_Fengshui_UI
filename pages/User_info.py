import time
from common.base import BaseApp
from pages.Always_allow import Power
from common.start import start_app
'''用户信息页面元素抓取'''

class User_info(BaseApp):
    ''' 用户信息页面'''
    loc1 = {"name": "点击头像", "by": "id", "value": "com.mmc.fengshui.pass:id/ivUserAvatar"}
    loc2 = {"name": "点击我的昵称", "by": "text", "value": "我的昵称"}
    loc3 = {"name": "点击我的生日", "by": "text", "value": "我的生日"}
    loc4 = {"name": "点击我的需求", "by": "text", "value": "我的需求"}
    loc5 = {"name": "点击我的性别", "by": "text", "value": "我的性别"}
    loc6 = {"name": "点击工作状况", "by": "text", "value": "工作状况"}
    loc7 = {"name": "点击婚姻状况", "by": "text", "value": "婚姻状况"}
    loc8 = {"name": "点击手机号码", "by": "text", "value": "手机号码"}
    loc9 = {"name": "点击修改密码", "by": "text", "value": "修改密码"}
    loc10 = {"name": "点击修改昵称输入框", "by": "id", "value": "com.mmc.fengshui.pass:id/linghit_profile_nick_name_et"}
    loc11 = {"name": "点击修改昵称取消", "by": "text", "value": "取消"}
    loc12 = {"name": "点击修改昵称确定", "by": "text", "value": "确定"}
    loc13 = {"name": " 我的资料", "by": "text", "value": "我的资料"}
    loc14 = {"name": " 点击退出登录", "by": "text", "value": "退出登录"}
    loc15 = {"name": " 点击关闭需求弹框", "by": "text", "value": "以后再选"}
    loc16 = {"name": " 点击性别男", "by": "text", "value": "男"}
    loc17 = {"name": " 点击工作状况", "by": "text", "value": "待业"}
    loc18 = {"name": " 点击婚姻状况", "by": "text", "value": "单身"}
    loc19 = {"name": " 点击手机号码跳转界面", "by": "text", "value": "风水罗盘"}
    loc20 = {"name": "点击课程tab", "by": "id", "value": "com.mmc.fengshui.pass:id/vBCNavigationTab5"}
    loc21 = {"name": " 点击出生日期弹框", "by": "text", "value": "确定"}

    def step_01(self):
        '''点击头像进入我的资料界面'''
        size = self.driver.get_window_size()  # 获取手机屏幕
        self.driver.swipe(size['width'] / 2, size['height']  / 4, size['width'] / 2, size['height']  * 3 / 4,
                          5000)  # 滑动界面到底部
        time.sleep(3)
        time.sleep(2)
        self.click(self.loc1)
        time.sleep(3)
        self.is_element_exist(self.loc13)

    def step_02(self):
        '''点击我的昵称'''
        time.sleep(2)
        self.click(self.loc2)
        time.sleep(3)

    def step_03(self):
        '''点击我的昵称-取消'''
        time.sleep(2)
        self.click(self.loc11)
        time.sleep(2)

    def step_04(self):
        '''点击我的生日'''
        time.sleep(3)
        self.click(self.loc3)
        time.sleep(3)
        self.click(self.loc21)
        time.sleep(5)

    def step_05(self):
        '''点击我的需求'''
        time.sleep(2)
        self.click(self.loc4)
        time.sleep(2)
        self.click(self.loc15)
        time.sleep(5)

    def step_06(self):
        '''点击我的性别'''
        time.sleep(3)
        self.click(self.loc5)
        time.sleep(3)
        self.click(self.loc16)
        time.sleep(3)

    def step_07(self):
        '''点击工作状况'''
        time.sleep(3)
        self.click(self.loc6)
        time.sleep(3)
        self.click(self.loc17)
        time.sleep(3)

    def step_08(self):
        '''点击婚姻状况'''
        time.sleep(3)
        self.click(self.loc7)
        time.sleep(3)
        self.click(self.loc18)
        time.sleep(3)

    def step_09(self):
        '''点击手机号码'''
        time.sleep(3)
        self.click(self.loc8)
        time.sleep(8)
        self.is_element_exist(self.loc19)
        self.driver.back()
        time.sleep(3)


    def step_10(self):
        '''点击修改密码'''
        time.sleep(3)
        self.click(self.loc9)
        time.sleep(3)
        self.driver.back()
        time.sleep(3)

    def step_11(self):
        '''点击我的昵称-点击确定'''
        time.sleep(3)
        self.click(self.loc12)
        time.sleep(3)

    def step_12(self):
        '''点击导航栏课程tab'''
        time.sleep(3)
        self.click(self.loc20)
        time.sleep(3)

    def step_13(self):
        '''点击退出登录'''
        time.sleep(3)
        self.click(self.loc14)
        time.sleep(3)

