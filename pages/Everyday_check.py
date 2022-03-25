import time
from common.base import BaseApp
from pages.Always_allow import Power
from common.start import start_app
'''签到页面元素抓取'''

class Everyday_check(BaseApp):
    ''' 登录页面'''
    loc1 = {"name": "查看今日运势", "by": "text", "value": "查看今日运势"}
    loc2 = {"name": "签到", "by": "text", "value": "签到"}
    loc3 = {"name": "查看我的优惠券", "by": "text", "value": "查看我的优惠券"}

    def step_01(self):
        '''点击查看今日运势'''
        time.sleep(2)
        self.click(self.loc1)


    def step_02(self):
        '''点击签到'''
        time.sleep(2)
        self.click(self.loc2)
        time.sleep(2)

    def step_03(self):
        '''查看优惠券'''
        time.sleep(2)
        self.click(self.loc3)
        time.sleep(1)
        self.driver.back()
        time.sleep(2)
