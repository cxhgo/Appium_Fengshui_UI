# coding:utf-8
from appium import webdriver

des_leidian = {
                "platformName": "Android",  # 设备系统
                "deviceName": "655S5S9DPZMBDYBQ",  # 设备名称，adb devices查看
                "platformVersion": "6.0",  # 手机或模拟器的版本号
                "appPackage": "com.mmc.fengshui.pass",  # apk包名
                "appActivity": "com.mmc.fengshui.pass.ui.activity.MainActivity",  # 打开的进程名
                "noReset": True,  # 应用不重置
                "udid": "655S5S9DPZMBDYBQ",   # 识别手机唯一标识
                'unicodeKeyboard': True,   # appium自带键盘
                'resetKeyboard': True,     # 解决中文乱码问题
                'noSign': True,
                "automationName": "Uiautomator2",  # toast 必须用Uiautomator2
                "autoGrantPermissions": True
                }

des_yeshen = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "platformVersion": "7.1.2",
                "appPackage": "com.mmc.fengshui.pass",
                "appActivity": "com.mmc.fengshui.pass.ui.activity.MainActivity",
                "noReset": True,
                "udid": "emulator-5554",   # 识别手机唯一标识
                "automationName": "Uiautomator2",  # toast 必须用Uiautomator2
                "autoGrantPermissions": True,
                'unicodeKeyboard': True,   # appium自带键盘
                'resetKeyboard': True,     # 解决中文乱码问题
                }


def start_app(deviceName="yeshen", port=4720):
    '''启动app'''
    if deviceName == "leidian":
        des = des_leidian
    elif deviceName == "yeshen":
        des = des_yeshen
    else:
        des = des_leidian
    driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % port, des)
    return driver
if __name__ == '__main__':
    driver = start_app()