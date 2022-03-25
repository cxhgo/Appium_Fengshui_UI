import time
from common.base import BaseApp
from pages.Always_allow import Power
from common.start import start_app
'''用户信息页面元素抓取'''

class Course(BaseApp):
   loc1 = {"name": "点击优惠券", "by": "text", "value": "优惠券（0）"}
   loc2 = {"name": "点击课程tab", "by": "id", "value": "com.mmc.fengshui.pass:id/vBCNavigationTab5"}
   loc3 = {"name": "点击风水记录", "by": "text", "value": "风水记录"}
   loc4 = {"name": "点击宅主分析", "by": "text", "value": "宅主分析"}
   loc5 = {"name": "点击服务消息", "by": "text", "value": "服务消息"}
   loc6 = {"name": "点击祈福明灯", "by": "text", "value": "祈福明灯"}
   loc7 = {"name": "点击藏宝阁", "by": "text", "value": "藏宝阁"}
   loc8 = {"name": "点击设置", "by": "text", "value": "设置"}
   loc9 = {"name": "跳转优惠券", "by": "text", "value": "优惠券"}
   loc10 = {"name": "跳转消息列表", "by": "text", "value": "消息列表"}
   loc11 = {"name": "跳转消息列表", "by": "text", "value": "我的明灯"}
   loc12 = {"name": "跳转消息列表", "by": "text", "value": "我的圣品"}
   loc13 = {"name": "跳转消息列表", "by": "text", "value": "应用设置"}

   def step_01(self):
      '''点击导航栏课程tab'''
      time.sleep(2)
      self.click(self.loc2)
      time.sleep(3)
      size = self.driver.get_window_size()  # 获取手机屏幕
      self.driver.swipe(size['width'] / 2, size['height'] * 3 / 4, size['width'] / 2, size['height'] / 4,5000)  # 滑动界面到底部
      time.sleep(3)

   def step_02(self):
      '''点击优惠券'''
      time.sleep(2)
      self.click(self.loc1)
      time.sleep(3)
      self.is_element_exist(self.loc9)
      time.sleep(3)
      self.driver.back()
      time.sleep(3)

   def step_03(self):
       '''点击风水记录'''
       time.sleep(2)
       self.click(self.loc3)
       time.sleep(4)
       self.is_element_exist(self.loc3)
       time.sleep(3)
       self.driver.back()
       time.sleep(2)

   def step_04(self):
       '''点击宅主分析'''
       time.sleep(2)
       self.click(self.loc4)
       time.sleep(4)
       self.is_element_exist(self.loc4)
       time.sleep(2)
       self.driver.back()
       time.sleep(2)

   def step_05(self):
       '''点击服务消息'''
       time.sleep(2)
       self.click(self.loc5)
       time.sleep(4)
       self.is_element_exist(self.loc10)
       time.sleep(2)
       self.driver.back()
       time.sleep(2)

   def step_06(self):
       '''点击祈福明灯'''
       time.sleep(2)
       self.click(self.loc6)
       time.sleep(4)
       self.is_element_exist(self.loc11)
       time.sleep(2)
       self.driver.back()
       time.sleep(2)

   def step_07(self):
       '''点击藏宝阁'''
       time.sleep(2)
       self.click(self.loc7)
       time.sleep(4)
       self.is_element_exist(self.loc12)
       time.sleep(2)
       self.driver.back()
       time.sleep(2)

   def step_08(self):
       '''点击设置'''
       time.sleep(2)
       self.click(self.loc8)
       time.sleep(4)
       self.is_element_exist(self.loc13)
       time.sleep(2)
       self.driver.back()
       time.sleep(2)

