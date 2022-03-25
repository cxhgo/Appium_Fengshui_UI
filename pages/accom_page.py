# -*- encoding:utf-8 -*-
import time
from common.base import BaseApp
'''陪聊页面元素抓取'''


class Voice(BaseApp):
    '''陪聊页面-'''
    def step_01(self):
        '''陪聊页面-测试邀约功能点:选择15分钟点击立即邀约'''
        loc1 = {"name": "点击", "by": "id", "value": "com.mmc.fengshui.pass:id/linghit_quick_login_btn"}
        loc2 = {"name": "点击声优聊天", "by": "id", "value": "com.mmc.feelsowarm:id/skill_icon_iv"}
        loc3 = {"name": "点击邀约", "by": "id", "value": "com.mmc.feelsowarm:id/accompany_live_info_show_dialog"}
        loc4 = {"name": "点击15分钟", "by": "id", "value": "com.mmc.feelsowarm:id/accompany_dialog_try_to_chat_price_30"}
        loc5 = {"name": "点击立即邀约", "by": "id", "value": "com.mmc.feelsowarm:id/accompany_dialog_try_to_chat_go"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/mine_web_back"}

        self.click(loc1)
        self.click(loc2)
        time.sleep(2)
        self.driver.tap([(274, 1012), (537, 1275)], 500)
        time.sleep(2)
        self.click(loc3)
        self.click(loc4)
        self.click(loc5)
        self.click(loc6)

    def step_02(self):
        '''陪聊页面-测试邀约功能点:选择30分钟点击立即邀约'''
        loc1 = {"name": "点击邀约", "by": "id", "value": "com.mmc.feelsowarm:id/accompany_live_info_show_dialog"}
        loc2 = {"name": "点击30分钟", "by": "id", "value": "com.mmc.feelsowarm:id/accompany_dialog_try_to_chat_price_60"}
        loc3 = {"name": "点击立即邀约", "by": "id", "value": "com.mmc.feelsowarm:id/accompany_dialog_try_to_chat_go"}
        loc4 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/mine_web_back"}
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
        self.click(loc4)

    def step_03(self):
        '''陪聊页面-测试拉黑功能点'''
        loc1 = {"name": "点击Hi", "by": "id", "value": "com.mmc.feelsowarm:id/accompany_live_info_im"}
        loc2 = {"name": "点击聊天设置", "by": "id", "value": "com.mmc.feelsowarm:id/message_chatroom_setting"}
        self.click(loc1)
        self.click(loc2)
        ru1 = self.driver.find_element_by_id("com.mmc.feelsowarm:id/message_setting_black").text
        if ru1 == "拉黑":
            self.driver.find_element_by_id("com.mmc.feelsowarm:id/message_setting_black").click()
            self.driver.find_element_by_id("com.mmc.feelsowarm:id/message_setting_black_confirm").click()
        elif ru1 == "取消拉黑":
            self.driver.find_element_by_id("com.mmc.feelsowarm:id/message_setting_black").click()

    def step_04(self):
        '''陪聊页面-测试举报功能点'''
        loc1 = {"name": "点击聊天设置", "by": "id", "value": "com.mmc.feelsowarm:id/message_chatroom_setting"}
        loc2 = {"name": "点击举报", "by": "id", "value": "com.mmc.feelsowarm:id/message_setting_jubao"}
        loc3 = {"name": "点击发布不适当内容对我造成骚扰", "by": "id", "value": "com.mmc.feelsowarm:id/user_report_reason_harassment"}
        loc4 = {"name": "输入举报内容", "by": "id", "value": "com.mmc.feelsowarm:id/user_report_describe_ed"}
        loc5 = {"name": "点击提交", "by": "id", "value": "com.mmc.feelsowarm:id/user_report_commit_tv"}
        loc6 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/message_chatroom_back"}
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
        self.send_text(loc4,u"骚扰我了")
        self.click(loc5)
        self.click(loc6)
        print(self.is_toast_exist("举报成功"))

    def step_05(self):
        '''陪聊页面-测试关注功能点'''
        try:
            self.driver.find_element_by_id("com.mmc.feelsowarm:id/accompany_live_info_attention")
            print("关注成功 ")
        except:
            print("已关注该用户")
            pass

    def step_06(self):
        '''陪聊页面-测试TA的主页:邀他传图功能点'''
        loc1 = {"name": "点击TA的主页", "by": "id", "value": "com.mmc.feelsowarm:id/accompany_live_info_attention"}
        try:
            self.driver.find_element_by_id("com.mmc.feelsowarm:id/accompany_live_info_attention").click()
        except:
            pass
        try:
            self.click(loc1)
        except:
            pass
        try:
            self.driver.find_element_by_id("com.mmc.feelsowarm:id/invite_upload_photo_view").click()
            self.driver.find_element_by_id("com.mmc.feelsowarm:id/message_chatroom_back").click()
            print("邀请成功")
        except:
            pass

    def step_07(self):
        '''陪聊页面-测试TA的主页，分享我的图片'''
        loc1 = {"name": "点击分享", "by": "id", "value": "com.mmc.feelsowarm:id/mine_personal_home_share"}
        loc2 = {"name": "点击分享我的图片", "by": "id", "value": "com.mmc.feelsowarm:id/mine_activity_mine_share_preview_share"}
        loc3 = {"name": "点击关闭", "by": "id", "value": "com.mmc.feelsowarm:id/share_close"}
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)

    def step_08(self):
        '''陪聊页面-测试TA的主页，分享-保存到相册'''
        loc1 = {"name": "点击保存到相册", "by": "id", "value": "com.mmc.feelsowarm:id/mine_activity_mine_share_preview_save_pic"}
        loc2 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/mine_activity_mine_share_preview_back"}
        self.click(loc1)
        self.click(loc2)

    def step_09(self):
        '''陪聊页面-获取该用户看过的数量'''
        reu = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_homepage_huozan_num").text
        print("看过的数量为%s" % reu)

    def step_10(self):
        '''陪聊页面-获取该用户关注数量'''
        reu = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_homepage_guanzhu_num").text
        print("关注数量为%s" % reu)

    def step_11(self):
        '''陪聊页面-获取该用户粉丝数量'''
        reu = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_homepage_fans_num").text
        print("粉丝数量为%s" % reu)

    def step_12(self):
        '''陪聊页面-获取该用户暖流号'''
        loc1 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/mine_personal_home_back"}
        loc2 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/accompany_back"}
        loc3 = {"name": "点击返回", "by": "desc", "value": "转到上一层级"}
        ru = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_personal_home_title").text
        print(ru)
        time.sleep(5)
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)

    def step_13(self):
        '''陪聊页面-测试情感星球标签'''
        loc2 = {"name": "点击返回", "by": "desc", "value": "转到上一层级"}
        self.driver.find_elements_by_id("com.mmc.feelsowarm:id/skill_icon_iv")[1].click()
        self.click(loc2)

    def step_14(self):
        '''陪聊页面-测试恋爱达人标签'''
        loc2 = {"name": "点击返回", "by": "desc", "value": "转到上一层级"}
        self.driver.find_elements_by_id("com.mmc.feelsowarm:id/skill_icon_iv")[2].click()
        self.click(loc2)

    def step_15(self):
        '''陪聊页面-测试游戏标签'''
        loc2 = {"name": "点击返回", "by": "desc", "value": "转到上一层级"}
        self.driver.find_elements_by_id("com.mmc.feelsowarm:id/skill_icon_iv")[3].click()
        self.click(loc2)