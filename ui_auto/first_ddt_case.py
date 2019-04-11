import unittest
import ddt
import os
import sys
sys.path.append("E:/ui_auto")
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
from util.excel_util import ExcelUtil

#邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息

ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    @classmethod   #装饰器
    def setUpClass(cls):
        print("所有case 执行之前的前置")

    @classmethod  # 装饰器
    def tearDownClass(cls):
        print("所有case执行之后的后置")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
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

    # @ddt.data(
    # ["123","mushishi01","111111","code","email_error","请输入有效的电子邮件地址"],
    # ["@qq.com", "mushishi01", "111111", "code", "email_error", "请输入有效的电子邮件地址"],
    # ["12wewe@qq.com", "mushishinxnxn", "111111", "code", "email_error", "请输入有效的电子邮件地址"]
    # #["12@qq.com", "mushishi01", "111111", "code", "email_error", "请输入有效的电子邮件地址"],
    # #["12@qq.com", "mushishi01", "111111", "code", "email_error", "请输入有效的电子邮件地址"]
    #     )
    # @ddt.unpack

    @ddt.data(*data)
    def test_register_case(self,data):
        email, username, password, code, assertCode, assertText = data
        email_error = self.login.register_function(email,username,password,code,assertCode,assertText)
        print(email_error)
        self.assertFalse(email_error,"测试失败")



if __name__ == '__main__':
    file_path = os.path.join(os.getcwd() + "/report/" + "first_ddt_test_report.html")
    f = open(file_path, "wb")
    suite = unittest.TestLoader(). loadTestsFromTestCase(FirstDdtCase)
   # unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report1", description="这是我的第一个test case1")
    runner.run(suite)

    #unittest.main()

