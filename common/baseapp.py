from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from common import keyevent
import os
class Base():
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.a = self.driver.get_window_size()


    def find(self,locator):
        '''locator-->{"by" ,"value":"xxxx"}
        {"by":text", "value":"注册/登录"}
        '''
        if "desc" in locator["by"]:
            element = WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_element_by_accessibility_id(locator['value']))
        elif "android" in locator["by"]:
            element = WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_element_by_android_uiautomator(locator['value']))
        elif "text" in locator["by"]:
            t = locator["value"]
            xpath_text = '//*[@text="%s"]' % t
            element = WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_element_by_xpath(xpath_text))
        else:
            element = WebDriverWait(self.driver, 30, 0.5).until(Ec.presence_of_element_located(locator))
        return element


    def swipeUp(self, duration=500, t=1):
        # 向上滑动屏幕
        start_x = self.a['width']/2
        start_y = self.a['height']/5*4

        end_x = self.a['width']/2
        end_y = self.a['height']/5*1
        for i in range(t):
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def swipeDown(self, duration=500, t=1):
        # 向下滑动屏幕
        start_x = self.a['width']/2
        start_y = self.a['height']/5*1
        end_x = self.a['width']/2
        end_y = self.a['height']/5*4
        for i in range(t):
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)


    def tap_new(self,el=None, x=None, y=None,count=1):
        '''坐标定位'''
        action = TouchAction(self.driver)
        if el is not None:
            action.tap(element=el, count=count).perform()   # 传元素对象
        else:
            action.tap(x=x, y=y, count=count).perform()









