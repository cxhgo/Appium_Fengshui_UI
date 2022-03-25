# -*- encoding:utf-8 -*-
'''发现页面元素抓取'''
from common.base import BaseApp
import time
from appium.webdriver.common.touch_action import TouchAction


class Cancel(BaseApp):
    '''动态'''
    def step_01(self):
        '''测试关注功能点'''
        loc1 = {"name": "点击动态按钮", "by": "text", "value": "动态"}
        time.sleep(10)
        self.click(loc1)
        self.swipe_up()
        try:
            self.driver.find_element_by_id("com.mmc.feelsowarm:id/mDynamicSquareGuestAttention").click()
            print("关注成功")
        except:
            print("已关注")
            time.sleep(5)

    def step_02(self):
        '''测试打赏功能点'''
        loc1 = {"name": "点击赏", "by": "id", "value": "com.mmc.feelsowarm:id/mDynamicSquareReward"}
        loc2 = {"name": "点击打赏", "by": "id", "value": "com.mmc.feelsowarm:id/listen_reward_submit"}
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.click(loc1)
        self.click(loc2)

    def step_03(self):
        '''测试评论功能点'''
        loc1 = {"name": "点击弹", "by": "id", "value": "com.mmc.feelsowarm:id/mDynamicSquareComment"}
        loc2 = {"name": "输入内容", "by": "id", "value": "com.mmc.feelsowarm:id/vImageDynamicDetailInput"}
        loc3 = {"name": "点击发送", "by": "id", "value": "com.mmc.feelsowarm:id/vImageDynamicDetailSend"}
        self.click(loc1)
        self.send_text(loc2, "呵呵")
        self.click(loc3)

    def step_04(self):
        '''获取评论人数'''
        reu = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mDynamicSquareCommentNumber").text
        print("评论人数为 %s" % reu)

    def step_05(self):
        '''获取看过的人数'''
        try:
            reu = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mDynamicSquareLookTv").text
            print(reu)
        except:
            pass

    def step_06(self):
        '''发布动态:文字'''
        loc1 = {"name": "点击发布按钮", "by": "id", "value": "com.mmc.feelsowarm:id/mDynamicRelease"}
        loc2 = {"name": "输入内容", "by": "id", "value": "com.mmc.feelsowarm:id/vContentTextEd"}
        loc3 = {"name": "点击发布", "by": "text", "value": "发布"}
        loc4 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/mine_personal_home_back"}
        self.click(loc1)
        self.send_text(loc2, "葡萄牙")
        self.click(loc3)
        self.click(loc4)

    def step_07(self):
        '''发布动态:图片'''
        loc1 = {"name": "点击发布按钮", "by": "id", "value": "com.mmc.feelsowarm:id/mDynamicRelease"}
        loc2 = {"name": "相机", "by": "id", "value": "com.mmc.feelsowarm:id/select_pic_iv"}
        loc3 = {"name": "点击图片", "by": "id", "value": "com.mmc.feelsowarm:id/media_item_check"}
        loc4 = {"name": "点击确定", "by": "id", "value": "com.mmc.feelsowarm:id/choose_ok_btn"}
        loc5 = {"name": "点击发布", "by": "text", "value": "发布"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/mine_personal_home_back"}
        self.click(loc1)
        self.click(loc2)
        self.driver.find_elements_by_id("com.mmc.feelsowarm:id/media_item_check")[-1].click()
        self.click(loc4)
        self.click(loc5)
        self.click(loc6)

    def step_08(self):
        '''发布动态:音频'''
        loc1 = {"name": "点击发布按钮", "by": "id", "value": "com.mmc.feelsowarm:id/mDynamicRelease"}
        loc2 = {"name": "音频", "by": "id", "value": "com.mmc.feelsowarm:id/select_record_iv"}
        loc5 = {"name": "点击发布", "by": "text", "value": "发布"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/mine_personal_home_back"}
        self.click(loc1)
        self.click(loc2)
        time.sleep(5)
        el = self.driver.find_element_by_id("com.mmc.feelsowarm:id/vDynamicSquareRecord")
        action1 = TouchAction(self.driver)
        action1.long_press(el=el, duration=10000).wait(5000).perform()
        self.click(loc5)
        self.click(loc6)

    def step_09(self):
        '''举报'''
        loc1 = {"name": "点击发布按钮", "by": "id", "value": "com.mmc.feelsowarm:id/mDynamicSquareMore"}
        loc2 = {"name": "点击举报", "by": "id", "value": "com.mmc.feelsowarm:id/discover_item_dialog_more_report"}
        loc3 = {"name": "点击政治敏感", "by": "id", "value": "com.mmc.feelsowarm:id/user_report_reason_political"}
        loc4 = {"name": "输入政治敏感", "by": "id", "value": "com.mmc.feelsowarm:id/user_report_describe_ed"}
        loc5 = {"name": "点击提交", "by": "id", "value": "com.mmc.feelsowarm:id/user_report_commit_tv"}
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
        self.send_text(loc4, "政治敏感")
        self.click(loc5)

