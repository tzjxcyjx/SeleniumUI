import unittest
class FirstCase01(unittest.TestCase):
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
    @unittest.skip("不执行第一条")
    def testfirst01(self):
        print("this is first case")
    def testfirst03(self):
        print("this is second case")

    def testfirst02(self):
        print("this is third case")

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01("testfirst02"))
    suite.addTest(FirstCase01("testfirst01"))
    suite.addTest(FirstCase01("testfirst03"))
    unittest.TextTestRunner().run(suite)
