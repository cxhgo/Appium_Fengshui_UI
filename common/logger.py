# coding:utf-8
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
import logging, time
import inspect

# log_path是存放日志的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path): os.mkdir(log_path)


def get__function_name():
    '''获取正在运行函数(或方法)名称'''
    return inspect.stack()[1][3]


class Log():
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        # self.formatter = logging.Formatter('[%(asctime)s]-%(levelname)s: %(message)s')

        self.formatter = logging.Formatter("[%(levelname)s]--%(asctime)s-%(filename)s->%(funcName)s->%(module)s line:%(lineno)d: %(message)s")

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        # fh = logging.FileHandler(self.logname, 'a')  # 追加模式  这个是python2的
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        '''inspect.stack()获取当前运行代码的方法名，和行数'''
        msg = "%s__ %s line%s" % (inspect.stack()[1][3], message, inspect.stack()[1][2])
        self.__console('debug', msg)

    def info(self, message):
        msg = "%s__ %s line%s" % (inspect.stack()[1][3], message, inspect.stack()[1][2])
        self.__console('info', msg)

    def warning(self, message):
        msg = "%s__ %s line%s" % (inspect.stack()[1][3], message, inspect.stack()[1][2])
        self.__console('warning', msg)

    def error(self, message):
        msg = "%s__ %s line%s" % (inspect.stack()[1][3], message, inspect.stack()[1][2])
        self.__console('error', msg)

