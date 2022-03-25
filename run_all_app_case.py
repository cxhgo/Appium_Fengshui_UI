# coding:utf-8
import os
import unittest
import time
from common import HTMLTestRunner_cn
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

cur_path = os.path.dirname(os.path.realpath(__file__))


def add_case(caseName="case", rule="test*.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)  # 用例文件夹
    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("test case path:%s" % case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    print(discover)
    return discover


def run_case(all_case, reportName="report"):
    '''第二步：执行所有的用例, 并把结果写入HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)  # 用例文件夹
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, "result.html")
    print("report path:%s"%report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                           retry=1,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print(u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send_mail(report):
    '''第四步：发送最新的测试报告内容'''
    with open(report, "rb") as f:
        mail_body = f.read()
    f.close()
    # 定义邮件内容
    # sendfile = open(report, 'rb').read()
    Sender = "chenxiaohuan@linghit.com"
    Pwd = "Cxh940107"
    Hoster = "smtp.exmail.qq.com"
    port = 465
    receiver = "chenxiaohuan@linghit.com"
    titles = 'android风水罗盘通用功能'
    Subject = "【自动化测试】" + titles
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header("Content-Disposition", "attachment",filename=("gbk", "", time.strftime("%Y-%m-%d %H_%M_%S") + "report.html"))
    msg = MIMEMultipart('related')
    msg.attach(att)
    msgtext = MIMEText(mail_body,'html','utf-8')
    msg.attach(msgtext)
    msg['Subject'] = Subject
    msg['From'] = Sender
    msg['To'] = ''.join(receiver)
    # 发送邮件连接
    try:
        # server = smtplib.SMTP()
        server = smtplib.SMTP_SSL(Hoster, port)
        server.set_debuglevel(1)  # 设置输出debug调试信息，默认不输出
        # server.connect(Hoster)
        # server.ehlo()# 使用ehlo指令像ESMTP（SMTP扩展）确认你的身份
        # server.starttls()# 使SMTP连接运行在TLS模式，所有的SMTP指令都会被加密
        server.login(Sender, Pwd)
        server.sendmail(Sender, receiver, msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print("失败: " + str(e))

if __name__ == "__main__":
    all_case = add_case()   # 1加载用例
    # # 生成测试报告的路径
    run_case(all_case)        # 2执行用例
    # # 获取最新的测试报告文件
    report_path = os.path.join(cur_path, "report")
    report = get_report_file(report_path)
    #邮箱配置  邮箱配置可以写到yaml文件
    send_mail(report)


