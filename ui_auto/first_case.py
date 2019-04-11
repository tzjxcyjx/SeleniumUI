import os
import sys
sys.path.append("E:/ui_auto")
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
from log.user_log import UserLog

class FirstCase(unittest.TestCase):
    @classmethod   #装饰器
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        print("所有case 执行之前的前置")

    @classmethod  # 装饰器
    def tearDownClass(cls):
        cls.log.close_handle()
        print("所有case执行之后的后置")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.logger.info("this is chrome")
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        #if sys.exc_info()[0]:
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + "/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
        print("这是case 的后置条件")


    # 邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息


    def test_login_email_error(self):
        email_error = self.login.login_email_error("134@qq.com","user12","111111","test1")
        # if email_error == True:
        #     print("注册成功了，此条case失败")
        #通过assert 判断是否为error
        self.assertFalse(email_error,"测试失败")

    def test_username_error(self):
        user_name_error = self.login.login_username_error("123@qq.com","ss","111111","test1")
        self.assertFalse(user_name_error,"测试失败")

    def test_password_error(self):
        password_error = self.login.login_password_error("122@qq.com","user2222","111111","test1")
        self.assertFalse(password_error,"测试失败")


    def test_code_error(self):
        code_error = self.login.login_code_error("1234@qq.com","user3333","111111","test1")
        self.assertFalse(code_error,"测试失败")

    def test_login_success(self):
        success = self.login.login_success("12","user1111","111111","test1")
        self.assertFalse(success)
        
# def main():
#     first = FirstCase()
#     first.test_login_email_error()
#     first.test_username_error()
#     first.test_password_error()
#     first.test_code_error()
#     first.test_login_success()

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+"/report/"+"first_test_report.html")
    f = open(file_path,"wb")
    suite = unittest.TestSuite()
    suite.addTest(FirstCase("test_login_success"))
    suite.addTest(FirstCase("test_login_email_error"))
    suite.addTest(FirstCase("test_username_error"))
    suite.addTest(FirstCase("test_password_error"))
    suite.addTest(FirstCase("test_code_error"))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream = f,title="This is first report",description="这是我的第一个test case")
    runner.run(suite)
