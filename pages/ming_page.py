# -*- encoding:utf-8 -*-

'''我的页面元素抓取'''
from common.base import BaseApp
import time
from common.adb import adbKeyEvent
from common.keyevent import keyevent


class More(BaseApp):
    '''我的'''
    def step_01(self):
        '''获取看过人数'''
        try:
            time.sleep(2)
            self.driver.find_elements_by_id("com.mmc.feelsowarm:id/mian_layout_MessageNotificationView")[0].click()
            print("点击我的头像进入主页")
            time.sleep(10)
        except:
            time.sleep(2)
            self.driver.find_elements_by_id("com.mmc.feelsowarm:id/mian_layout_MessageNotificationView")[0].click()
            print("点击我的头像进入主页")
        reu = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_huozan_num").text
        print("看过的数量为%s" % reu)

    def step_02(self):
        '''获取关注人数'''
        reu = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_guanzhu_num").text
        print("关注人数为%s" % reu)

    def step_03(self):
        '''粉丝人数'''
        reu = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_fensi_num").text
        print("粉丝人数为%s" % reu)

    def step_04(self):
        '''收藏人数'''
        reu = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_shoucang_num").text
        print("收藏人数为%s" % reu)

    def step_06(self):
        '''获取暖流号'''
        reu = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_user_infor_user_number").text
        print(reu)
        time.sleep(2)

    def step_07(self):
        '''我的-设置-个人资料'''
        loc1 = {"name": "点击设置", "by": "id", "value": "com.mmc.feelsowarm:id/mine_user_infor_setting"}
        loc2 = {"name": "点击性别", "by": "id", "value": "com.mmc.feelsowarm:id/mine_setting_gender"}
        loc22 = {"name": "点击个人资料", "by": "id", "value": "com.mmc.feelsowarm:id/mine_setting_userdata"}
        loc3 = {"name": "选择男", "by": "id", "value": "com.mmc.feelsowarm:id/mine_gender_pick_male"}
        loc4 = {"name": "选择男", "by": "text", "value": "保存"}
        self.click(loc1)
        self.click(loc22)
        self.click(loc2)
        self.click(loc3)
        self.click(loc4)

    def step_08(self):
        '''我的-设置-账户管理'''
        loc1 = {"name": "点击账户管理", "by": "id", "value": "com.mmc.feelsowarm:id/mine_setting_account_manage"}
        loc2 = {"name": "点击更改密码", "by": "id", "value": "com.mmc.feelsowarm:id/mine_account_manage_changepwd"}
        loc3 = {"name": "输入密码", "by": "id", "value": "com.mmc.feelsowarm:id/login_change_password_input"}
        loc4 = {"name": "点击下一步", "by": "id", "value": "com.mmc.feelsowarm:id/login_change_password_next"}
        loc51 = {"name": "输入验证码", "by": "id", "value": "com.mmc.feelsowarm:id/tv_code1"}
        loc52 = {"name": "输入验证码", "by": "id", "value": "com.mmc.feelsowarm:id/tv_code2"}
        loc53 = {"name": "输入验证码", "by": "id", "value": "com.mmc.feelsowarm:id/tv_code3"}
        loc54 = {"name": "输入验证码", "by": "id", "value": "com.mmc.feelsowarm:id/tv_code4"}
        loc55 = {"name": "输入验证码", "by": "id", "value": "com.mmc.feelsowarm:id/tv_code5"}
        loc56 = {"name": "输入验证码", "by": "id", "value": "com.mmc.feelsowarm:id/tv_code6"}
        loc6 = {"name": "点击确定", "by": "id", "value": "com.mmc.feelsowarm:id/login_change_password_next"}
        loc7 = {"name": "点击登录/注册", "by": "id", "value": "com.mmc.feelsowarm:id/user_fragment_login_prompt_user_login"}
        loc8 = {"name": "点击密码登录", "by": "id", "value": "com.mmc.feelsowarm:id/password_login"}
        loc9 = {"name": "输入手机号", "by": "id", "value": "com.mmc.feelsowarm:id/code_login_phone"}
        loc10 = {"name": "输入密码", "by": "id", "value": "com.mmc.feelsowarm:id/login_phone_password"}
        loc11 = {"name": "点击登录", "by": "id", "value": "com.mmc.feelsowarm:id/password_login_comfire"}
        loc12 = {"name": "点击设置", "by": "id", "value": "com.mmc.feelsowarm:id/login_phone_password"}
        self.click(loc1)
        self.click(loc2)
        self.send_text(loc3, "123456")
        self.click(loc4)
        self.send_text(loc51, "1")
        self.send_text(loc52, "2")
        self.send_text(loc53, "3")
        self.send_text(loc54, "4")
        self.send_text(loc55, "5")
        self.send_text(loc56, "6")
        self.click(loc6)
        self.click(loc7)
        self.click(loc8)
        self.send_text(loc9, "18819447984")
        self.send_text(loc10, "123456")
        self.click(loc10)
        self.click(loc11)
        time.sleep(5)
        try:
            time.sleep(2)
            self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_user_infor_message").click()
            print("点击我的头像进入主页")
        except:
            time.sleep(2)
            self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_user_infor_message").click()
            print("点击我的头像进入主页")
        self.click(loc12)

    def step_09(self):
        '''我的-设置-陪伴师管理'''
        loc1 = {"name": "点击陪伴师管理", "by": "id", "value": "com.mmc.feelsowarm:id/mine_setting_company"}
        loc2 = {"name": "点击保存", "by": "id", "value": "com.mmc.feelsowarm:id/accompany_auth_info_submit"}
        self.click(loc1)
        self.click(loc2)

    def step_10(self):
        '''我的-设置-通知设置-私信'''
        loc1 = {"name": "点击通知设置", "by": "id", "value": "com.mmc.feelsowarm:id/mine_setting_message"}
        loc2 = {"name": "点击通知设置", "by": "id", "value": "com.mmc.feelsowarm:id/accompany_dialog_user_close_tips_ok"}
        self.click(loc1)
        adbKeyEvent(keyevent.KEYCODE_BACK)
        time.sleep(2)
        try:
            self.click(loc2)
        except:
            pass

    def step_11(self):
        '''我的-设置-通知设置-关注的人发内容'''
        loc1 = {"name": "点击通知设置", "by": "id", "value": "com.mmc.feelsowarm:id/message_setting_follow_people_notifacation"}
        try:
            self.click(loc1)
        except:
            pass

    def step_12(self):
        '''我的-设置-通知设置-倾听开播'''
        loc1 = {"name": "点击通知设置", "by": "id", "value": "com.mmc.feelsowarm:id/message_setting_start_broadcast"}
        try:
            self.click(loc1)
            time.sleep(3)
        except:
            time.sleep(3)

        adbKeyEvent(keyevent.KEYCODE_BACK)

    def step_13(self):
        '''我的-设置-隐私设置-谁可以发私信给我'''
        loc12 = {"name": "点击设置", "by": "id", "value": "com.mmc.feelsowarm:id/mine_user_infor_setting"}
        loc1 = {"name": "点击隐私设置", "by": "id", "value": "com.mmc.feelsowarm:id/mine_setting_privacy"}
        loc2 = {"name": "点击谁可以发私信给我", "by": "id", "value": "com.mmc.feelsowarm:id/mine_privacy_accept_privacy_msg"}
        loc3 = {"name": "选择仅互相关注的人 ", "by": "id", "value": "com.mmc.feelsowarm:id/mine_accept_privacy_group_2"}
        self.click(loc12)
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
        time.sleep(3)
        adbKeyEvent(keyevent.KEYCODE_BACK)
        time.sleep(2)
        adbKeyEvent(keyevent.KEYCODE_BACK)

    def step_14(self):
        '''我的-设置-隐私设置-黑名单'''
        loc1 = {"name": "点击隐私设置", "by": "id", "value": "com.mmc.feelsowarm:id/mine_setting_privacy"}
        loc2 = {"name": "点击黑名单", "by": "id", "value": "com.mmc.feelsowarm:id/mine_privacy_blacklist"}
        self.click(loc1)
        self.click(loc2)
        try:
            self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_black_item_follow_button").click()
            print("解除拉黑成功")
        except:
            pass
        time.sleep(3)
        adbKeyEvent(keyevent.KEYCODE_BACK)

    def step_15(self):
        '''我的-设置-隐私设置-私信自动回复'''
        loc1 = {"name": "点击私信自动回复", "by": "id", "value": "com.mmc.feelsowarm:id/mine_privacy_auto_send"}
        self.click(loc1)
        self.click(loc1)

    def step_16(self):
        '''我的-设置-隐私设置-私信自动打招呼内容'''
        loc1 = {"name": "点击私信自动打招呼内容", "by": "id", "value": "com.mmc.feelsowarm:id/mine_privacy_auto_send_content"}
        loc2 = {"name": "点击确认", "by": "id", "value": "com.mmc.feelsowarm:id/mine_release_edit_confirm"}
        self.click(loc1)
        self.click(loc2)
        adbKeyEvent(keyevent.KEYCODE_BACK)

    def step_17(self):
        '''我的-设置-清除缓存'''
        loc1 = {"name": "点击清除缓存", "by": "id", "value": "com.mmc.feelsowarm:id/mine_setting_clear_cache"}
        try:
            self.click(loc1)
            time.sleep(2)
        except:
            pass

        try:
            result = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_setting_clear_cache_size").text
            print("缓存还有%s" % result)
        except:
            pass

    def step_18(self):
        '''我的-设置-网络流量提醒'''
        loc1 = {"name": "点击网络流量提醒", "by": "id", "value": "com.mmc.feelsowarm:id/setting_network_traffic_alert"}
        self.click(loc1)
        adbKeyEvent(keyevent.KEYCODE_BACK)

    def step_19(self):
        '''我的-我的钱包-获取充值钱包余额'''
        loc1 = {"name": "点击我的钱包", "by": "id", "value": "com.mmc.feelsowarm:id/mine_n_coin_container"}
        time.sleep(2)
        self.swipe_up()
        time.sleep(2)
        self.click(loc1)
        result = self.driver.find_element_by_id("com.mmc.feelsowarm:id/ncoin_my_coin_balance").text
        print("获取充值钱包余额为%s" % result)

    def step_20(self):
        '''我的-我的钱包-获取收益钱包余额'''
        result = self.driver.find_element_by_id("com.mmc.feelsowarm:id/ncoin_my_coin_income").text
        print("获取收益钱包余额为%s" % result)

    def step_21(self):
        '''我的-我的钱包-获取陪伴师钱包余额'''
        try:
            result = self.driver.find_element_by_id("com.mmc.feelsowarm:id/ncoin_my_coin_accompany_income").text
            print("获取陪伴师钱包余额为%s" % result)
        except:
            pass

    def step_22(self):
        '''我的-我的钱包-钱包明细-支出N币'''
        loc1 = {"name": "点击钱包明细", "by": "id", "value": "com.mmc.feelsowarm:id/ncoin_record_the_detail"}
        self.click(loc1)
        result = self.driver.find_element_by_id("com.mmc.feelsowarm:id/ncoin_record_expenditure_count").text
        print("支出%s" % result)

    def step_23(self):
        '''我的-我的钱包-钱包明细-收入N币'''
        loc1 = {"name": "点击返回", "by": "desc", "value": "转到上一层级"}
        loc2 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/ncoin_my_coin_back"}
        result = self.driver.find_element_by_id("com.mmc.feelsowarm:id/ncoin_record_income_count").text
        print("收入%s" % result)
        self.click(loc1)
        self.click(loc2)

    def step_24(self):
        '''我的-财富等级-'''
        loc1 = {"name": "点击财富等级", "by": "id", "value": "com.mmc.feelsowarm:id/mine_n_wealth_container"}
        loc2 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/mine_activity_wealth_level_title_bar_back"}
        self.click(loc1)
        time.sleep(2)
        result = self.driver.find_element_by_id("com.mmc.feelsowarm:id/mine_wealth_level_tv").text
        print("财富等级为%s" % result)
        self.click(loc2)