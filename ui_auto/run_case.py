import unittest
import os
class RunCase(unittest.TestCase):
    def test_case01(self):
        case_path = os.path.join(os.getcwd(),"case")   #获取当前工程目录
        print(case_path)
        suite = unittest.defaultTestLoader.discover(case_path,"unittest_*.py")
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()

