#coding=utf-8
import logging
import os
import datetime
class UserLog:
    def __init__(self):
        #创建logger 对象
        self.logger = logging.getLogger()
        #设置logger 等级
        self.logger.setLevel(logging.DEBUG)

        #控制台输出日志
        consle = logging.StreamHandler()
        self.logger.addHandler(consle)
        #logger.debug("info")

        #文件名字
        print(os.path.abspath(__file__))  #输出当前文件绝对路径
        base_dir = os.path.dirname(os.path.abspath(__file__))
        print(base_dir)# 输出当前文件所在目录
        log_dir = os.path.join(base_dir,"logs") #进行目录的拼接
        #print(log_dir)

        #按照一定格式输出当前时间 "%Y-%m-%d"
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        # print(log_file)
        #log 文件
        log_name = log_dir +"/" + log_file
        print(log_name)

        #文件输出日志
        self.file_handle = logging.FileHandler(log_name,'a',encoding="utf-8")
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(filename)s -----> %(funcName)s %(levelno)s:%(levelname)s ----------> %(message)s")
        self.file_handle.setFormatter(formatter)
        #把logger 添加上handler
        self.logger.addHandler(self.file_handle)
        self.logger.debug("test1234123")
        print("********************")
        self.logger.debug('debug message') #debug 的message输出到控制台
        # self.logger.info('info message')
        # self.logger.warn('warn message')
        # self.logger.error('error message')
        # self.logger.critical('critical message')

        #logging.debug("test1234123")
        #print("testttttt1234")
        #consle.close()

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug("test")
    user.close_handle()