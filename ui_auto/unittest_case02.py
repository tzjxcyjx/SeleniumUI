import unittest
class FirstCase02(unittest.TestCase):
    @classmethod  # 装饰器
    def setUpClass(cls):
        print("所有case 执行之前的前置")
    @classmethod  # 装饰器
    def tearDownClass(cls):
        print("所有case执行之后的后置")
    def setUp(self):
        print("这是case 的前置条件")
    def tearDown(self):
        print("这是case 的后置条件")
    #@unittest.skip("不执行第一条")
    def testfirst001(self):
        print("this is 001 case")
    def testfirst003(self):
        print("this is 003 case")

    def testfirst002(self):
        print("this is 002 case")

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02("testfirst002"))
    suite.addTest(FirstCase02("testfirst001"))
    suite.addTest(FirstCase02("testfirst003"))
    unittest.TextTestRunner().run(suite)
