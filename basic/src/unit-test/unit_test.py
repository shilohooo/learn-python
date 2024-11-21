"""
python - 单元测试
"""
import unittest


def get_fullname(first_name, last_name):
    """
    格式化姓名
    :param first_name: 名字
    :param last_name: 姓氏
    :return: 姓名全称
    """
    return f"{first_name} {last_name}"


# 测试类需要继承 unittest.TestCase
class FullnameTestCase(unittest.TestCase):
    def setUp(self):
        """
        在测试开始前，执行此方法，可以在这里做一些初始化操作
        :return:
        """
        print('setUp')

    # 测试方法命名应以 test 开头
    def test_get_fullname(self):
        """
        测试获取姓名全称
        :return:
        """
        fullname = get_fullname('Bruce', 'Lee')
        # 通过 self.assertXXX 进行断言
        self.assertEqual(fullname, 'Bruce Lee')


# 执行单元测试
unittest.main()
