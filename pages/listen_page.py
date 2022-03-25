# -*- encoding:utf-8 -*-

'''消息页面元素抓取'''
from common.base import BaseApp



class Live(BaseApp):

    def step_01(self):
        '''发起私信'''
        loc1 = {"name": "点击消息", "by": "id", "value": "com.mmc.feelsowarm:id/main_message_view"}
        loc2 = {"name": "点击三", "by": "id", "value": "com.mmc.feelsowarm:id/message_main_more"}
        loc3 = {"name": "点击发起私信", "by": "id", "value": "com.mmc.feelsowarm:id/message_dialog_private_letter_send"}
        loc4 = {"name": "点击头像", "by": "id", "value": "com.mmc.feelsowarm:id/message_choose_friend_item_user_iv"}
        loc5 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/message_choose_friend_back"}

        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
        self.click(loc4)
        self.click(loc5)

    def step_02(self):
        '''清空私信'''
        loc1 = {"name": "点击三", "by": "id", "value": "com.mmc.feelsowarm:id/message_main_more"}
        loc2 = {"name": "点击清空私信", "by": "id", "value": "com.mmc.feelsowarm:id/message_dialog_private_letter_delete"}
        loc3 = {"name": "点击清空", "by": "id", "value": "com.mmc.feelsowarm:id/message_dialog_bottom_two_btn_submit"}
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)

    def step_03(self):
        '''新用户私信'''
        loc1 = {"name": "点击三", "by": "id", "value": "com.mmc.feelsowarm:id/message_main_more"}
        loc2 = {"name": "点击新用户私信", "by": "id", "value": "com.mmc.feelsowarm:id/message_dialog_private_new_user"}
        loc3 = {"name": "点击私信", "by": "id", "value": "com.mmc.feelsowarm:id/message_fans_item_follow_button"}
        loc4 = {"name": "点击私信", "by": "id", "value": "com.mmc.feelsowarm:id/message_chatroom_back"}
        loc5 = {"name": "点击私信", "by": "id", "value": "com.mmc.feelsowarm:id/vBackIv"}
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
        self.click(loc4)
        self.click(loc5)

    def step_04(self):
        '''评论'''
        loc1 = {"name": "点击三", "by": "id", "value": "com.mmc.feelsowarm:id/message_main_comment"}
        loc2 = {"name": "点击新用户私信", "by": "id", "value": "com.mmc.feelsowarm:id/message_comment_back"}
        self.click(loc1)
        self.click(loc2)

    def step_05(self):
        '''看过'''
        loc1 = {"name": "点击三", "by": "id", "value": "com.mmc.feelsowarm:id/message_main_zan"}
        loc2 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/message_praise_back"}
        self.click(loc1)
        self.click(loc2)

    def step_06(self):
        '''粉丝'''
        loc1 = {"name": "点击三", "by": "id", "value": "com.mmc.feelsowarm:id/message_main_fans"}
        loc2 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/message_fans_back"}
        loc3 = {"name": "点击返回", "by": "id", "value": "com.mmc.feelsowarm:id/message_main_back"}
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
