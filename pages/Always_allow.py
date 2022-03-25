from common.base import BaseApp
import time
from appium.webdriver.common.touch_action import TouchAction

from common.start import start_app
class Power(BaseApp):
    def always_allow(self,number=2):
       '''

       fuction:权限弹窗-始终允许
       args:1.传driver
       2.number，判断弹窗次数，默认给5次
       其它：
       WebDriverWait里面0.5s判断一次是否有弹窗，1s超时
       '''
       for i in range(number):
               # loc = ("xpath", "//*[@text='始终允许']")

           loc1 = {"name": "允许权限", "by": "text", "value": "允许"}
           try:
              self.click(loc1)
           except:
              pass

    def free_advert(self):
       loc2 = {"name": "广告弹框-立即免费咨询", "by": "id", "value": "com.mmc.fengshui.pass:id/vDialogBg"}
       self.click(loc2)

    def close_advert(self):
       loc3 = {"name": "关闭广告弹框", "by": "id", "value": "com.mmc.fengshui.pass:id/vDialogLeftClose"}
       self.click(loc3)

    def close_chouqian(self):
       loc4 = {"name": "关闭抽签广告", "by": "id", "value": "com.mmc.fengshui.pass:id/vDialogRightClose"}
       self.click(loc4)

    def close_jiaju(self):
       loc5 = {"name": "关闭家居风水广告", "by": "id", "value": "com.mmc.fengshui.pass:id/vDialogClose"}
       self.click(loc5)

    def close_luopan(self):
       loc6 = {"name": "关闭罗盘广告", "by": "class", "value": "android.widget.ImageView"}
       self.click(loc6)
       time.sleep(2)
       self.driver.back()
       time.sleep(2)

if __name__ == "__main__":
    # 调用始终允许函数
    driver = start_app()
    power = Power(driver)
    # Power(driver)
    time.sleep(4)
    power.close_advert()