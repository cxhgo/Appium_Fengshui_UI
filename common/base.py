
# coding:utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logger import Log
import time


class BaseApp():

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.fenbianlv = self.driver.get_window_size()
        # self.driver.find_element_by_accessibility_id()
        # self.driver.find_element_by_android_uiautomator()
        # self.driver.find_element()
        # self.driver.find_elements()
        self.log = Log()

    def find(self, locator):
        # locator 传字典  {"name": "输入账号", "by": "id", "value": "xxx", "timeout": "10"}

        # content-desc   # desc
        if "timeout" in locator:
            timeout = int(locator["timeout"])   # 转int
        else:
            timeout = 20
        if "name" in locator:
            self.log.info("点击\"%s\"" % locator['name']+",定位方法: %s-->%s" % (locator['by'], locator['value']))

        if locator["by"] == "desc":
            value = locator["value"]
            element = WebDriverWait(self.driver, timeout, 0.2).until(lambda x: x.find_element_by_accessibility_id(value))
        elif locator["by"] == "android":
            value = locator["value"]
            element = WebDriverWait(self.driver, timeout, 0.2).until(lambda x: x.find_element_by_android_uiautomator(value))
        elif locator["by"] == "class":
            value = locator["value"]
            element = WebDriverWait(self.driver, timeout, 0.2).until(lambda x: x.find_element_by_class_name(value))
        elif locator["by"] == "tap":
            value = locator["value"]
            element = WebDriverWait(self.driver, timeout, 0.2).until(lambda x: x.tap(value))
        elif locator["by"] == "text":
            value = "//*[@text='%s']" % locator["value"]
            _loc = ("xpath", value)
            element = WebDriverWait(self.driver, timeout, 0.2).until(EC.presence_of_element_located(_loc))
        else:
            loc = (locator["by"], locator["value"])  # 元祖
            element = WebDriverWait(self.driver, timeout, 0.2).until(EC.presence_of_element_located(loc))
        return element

    def finds(self, locator):
        # locator 传字典  {"name": "输入账号", "by": "id", "value": "xxx", "timeout": "10"}

        # content-desc   # desc
        if "timeout" in locator:
            timeout = int(locator["timeout"])   # 转int
        else:
            timeout = 30
        if "name" in locator:
            self.log.error("正在点击\"%s\"" %locator['name']+",定位方法: %s-->%s"% (locator['by'], locator['value']))

        if locator["by"] == "desc":
            value = locator["value"]
            elements = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_accessibility_id(value))
        elif locator["by"] == "android":
            value = locator["value"]
            elements = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_android_uiautomator(value))
        elif locator["by"] == "text":
            value = "//*[@text='%s']" % locator["value"]
            _loc = ("xpath", value)
            elements = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_all_elements_located(_loc))
        else:
            loc = (locator["by"], locator["value"])  # 元祖
            elements = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_all_elements_located(loc))
        return elements

    def click(self, locator):
        '''点击元素'''
        el = self.find(locator)
        el.click()

    def send_text(self, locator, text):
        '''发送文本'''
        el = self.find(locator)
        el.send_keys(text)

    def clear(self, locator):
        '''清空'''
        el = self.find(locator)
        el.clear()

    def swipe_up(self, n=1):
        '''
        往上滑
        :param driver:
        :return:  None
        '''
        x1 = self.fenbianlv['width']/2
        y1 = self.fenbianlv['height'] * 3 /4
        x2 = self.fenbianlv['width']/2
        y2 = self.fenbianlv['height'] /4
        for i in range(n):
            self.driver.swipe(x1, y1,  x2, y2, 500)

    def swipe_down(self, n=1):
        '''
        往下滑
        :param driver:
        :return: None
        '''
        x1 = self.fenbianlv['width']/2
        y1 = self.fenbianlv['height'] /4
        x2 = self.fenbianlv['width']/2
        y2 = self.fenbianlv['height'] * 3 /4
        for i in range(n):
            self.driver.swipe(x1, y1,  x2, y2, 500)

    def swipe_left(self, n=1):
        '''
        往左滑
        :param driver:
        :return: None
        '''
        x1 = self.fenbianlv['width']*3/4
        y1 = self.fenbianlv['height'] /2
        x2 = self.fenbianlv['width']/4
        y2 = self.fenbianlv['height'] /2
        for i in range(n):
            self.driver.swipe(x1, y1,  x2, y2, 500)

    def swipe_right(self, n=1):
        '''
        往右滑
        :param driver:
        :return: None
        '''
        x1 = self.fenbianlv['width']/4
        y1 = self.fenbianlv['height'] /2
        x2 = self.fenbianlv['width']*3 /4
        y2 = self.fenbianlv['height']  /2
        for i in range(n):
            self.driver.swipe(x1, y1,  x2, y2, 500)

    def is_toast_exist(self, text, timeout=30, poll_frequency=0.01):
        '''is toast exist, return True or False
        :Agrs:
         - driver - 传driver
         - text   - 页面上看到的文本内容
         - timeout - 最大超时时间，默认30s
         - poll_frequency  - 间隔查询时间，默认0.5s查询一次
        :Usage:
         is_toast_exist(driver, "看到的内容")
        '''
        try:

            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            t= WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            print("获取成功：toast为 %s" % str(t.text))
            return True
        except:
            print("获取toast失败")
            return False

    def is_toast_in(self, text):
        # 定位toast消息
        toast = ('xpath', '//*[contains(@text, "%s")]' % text)
        try:
            el = WebDriverWait(self.driver, 10, 0.2).until(EC.presence_of_element_located(toast))
            print(el.text)
            if text in el.text:
                return True
            else:
                return False
        except:
            return False

    def is_element_exist(self, locator):
        '''判断元素存在'''
        els = self.finds(locator)
        if len(els) < 1:
            return False
        else:
            return True

    def is_element_exist2(self,locator):
        try:
            self.find(locator)
            return True
        except:
            return False

    def tap_new(self,el=None, x=None, y=None,count=1):
        '''坐标定位'''
        action = TouchAction(self.driver)
        if el is not None:
            action.tap(element=el, count=count).perform()   # 传元素对象
        else:
            action.tap(x=x, y=y, count=count).perform()






