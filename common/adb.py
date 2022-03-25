# coding:utf-8
import os
from common.keyevent import keyevent


def adbKeyEvent(keycode):
    '''执行adbkeyevent事件'''
    cmd = "adb shell input keyevent %s" % keycode
    os.system(cmd)

def adbInput(text):
    '''adb 输入text文本内容，不能输入中文'''
    cmd = "adb shell input text %s" % text
    os.system(cmd)

def adbInput_text(text):
    '''adb 输入text文本内容，可以输入中文'''
    cmd = "adb shell am broadcast -a ADB_INPUT_TEXT --es msg text %s" % text
    os.system(cmd)

if __name__ == "__main__":
    adbInput_text("1452")
    adbInput_text("斑马")


