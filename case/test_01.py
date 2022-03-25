# coding:utf-8
import unittest
import time
from pages.Login import LoginPage
from common.logger import Log
from pages.Always_allow import Power
from pages.Everyday_check import Everyday_check
from pages.User_info import User_info
from pages.Course import Course
from pages.Register import Register
from pages.ForgetPwd import Forget_password
from common.start import start_app


class Test_01(unittest.TestCase):

    '''登录页面'''
    driver = None
    @classmethod
    def setUpClass(cls):
        time.sleep(10)
        cls.driver = start_app()
        cls.log = Log()
        cls.login = LoginPage(cls.driver)
        cls.power = Power(cls.driver)
        cls.every_check = Everyday_check(cls.driver)
        cls.register = Register(cls.driver)
        cls.forget_pwd = Forget_password(cls.driver)
        print("测试用例执行开始！")
        cls.driver.implicitly_wait(20)

    '''测试登录功能点：选择登录方式'''
    def test_01(self):
        self.power.close_advert()
        self.power.close_chouqian()
        self.power.close_jiaju()
        self.login.step_01()
        self.login.step_02()
        self.login.step_03()
        self.login.step_04()
        self.login.step_05()
        self.login.step_06()
        self.login.step_07()

    '''测试注册功能点'''
    def test_03(self):
        self.login.step_15()
        self.register.step_01()
        self.register.step_02()
        self.register.step_03()
        self.register.step_04()
        self.register.step_05()
        self.register.step_06()
        self.register.step_07()
        self.register.step_08()

    '''测试忘记密码功能点'''
    def test_04(self):
        self.login.step_16()
        self.forget_pwd.step_01()
        self.forget_pwd.step_02()
        self.forget_pwd.step_03()
        self.forget_pwd.step_04()
        self.forget_pwd.step_05()
        self.forget_pwd.step_06()
        self.forget_pwd.step_07()
        self.forget_pwd.step_08()
        self.login.step_16()
        self.forget_pwd.step_09()
        self.login.step_16()
        self.forget_pwd.step_10()

    '''测试登录功能点：进行账号密码登录'''
    def test_05(self):
        self.login.step_08()
        self.login.step_09()
        self.login.step_11()
        self.login.step_12()
        self.login.step_13()
        self.login.step_14()
        self.login.step_10()
        self.login.step_17()
        self.login.step_18()

    '''每日签到功能，已签到不需要执行step_02()，step_01()和step_03()只需要执行一个'''
    def test_06(self):
        # self.every_check.step_02()
        self.every_check.step_03()
    #     # self.every_check.step_01()

    @classmethod
    def tearDownClass(cls):
        print("测试用例执行结束！")
        cls.driver.quit()

class Test_02(unittest.TestCase):

    '''我的页面'''
    driver = None
    @classmethod
    def setUpClass(cls):
        time.sleep(10)
        cls.driver = start_app()
        cls.log = Log()
        cls.course = Course(cls.driver)
        cls.power = Power(cls.driver)
        print("测试用例执行开始！")
        # cls.cancel = Cancel(cls.driver)
        cls.driver.implicitly_wait(20)

    '''我的tab各跳转功能'''
    def test_01(self):
        self.power.close_advert()
        self.power.close_chouqian()
        self.course.step_01()
        self.course.step_02()
        self.course.step_03()
        self.course.step_04()
        self.course.step_05()
        self.course.step_06()
        self.course.step_07()
        self.course.step_08()


    @classmethod
    def tearDownClass(cls):
        print("测试用例执行结束！")
        cls.driver.quit()

class Test_03(unittest.TestCase):
    '''我的资料页面'''
    driver = None

    @classmethod
    def setUpClass(cls):
        time.sleep(10)
        cls.driver = start_app()
        cls.log = Log()
        cls.user_info = User_info(cls.driver)
        cls.power = Power(cls.driver)
        print("测试用例执行开始！")
        # cls.cancel = Cancel(cls.driver)
        cls.driver.implicitly_wait(20)

    '''我的资料各信息点击功能'''
    def test_01(self):
        self.power.close_advert()
        self.power.close_chouqian()
        self.user_info.step_12()
        self.user_info.step_01()
        self.user_info.step_02()
        self.user_info.step_03()
        self.user_info.step_04()
        self.user_info.step_05()
        self.user_info.step_06()
        self.user_info.step_07()
        self.user_info.step_08()
        self.user_info.step_09()
        self.user_info.step_10()
        self.user_info.step_13()


    @classmethod
    def tearDownClass(cls):
        print("测试用例执行结束！")
        cls.driver.quit()



if __name__ == "__main__":
    unittest.main()

