import ddt
import  unittest
@ddt.ddt #数据驱动类的特定关键字
class DataTest(unittest.TestCase):
    def setUp(self):
        print("这是setup")
    def tearDown(self):
        print("这是tearDown")
    #1,2 3,4 5,6
    #邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息
    # @ddt.data(
    #     [1,2,3,4],
    #     [3,4],
    #     [5,6]
    # )
    # @ddt.unpack  #数据驱动case前的特定关键字
    # def test_add(self,a,b):
    #     print(a + b)

    @ddt.data(
        [1, 2, 3, 4],
        [3, 4],
        [5, 6]
    )
    @ddt.unpack
    def test_1(self, value):
        print(value)


if __name__ == '__main__':
    unittest.main()
