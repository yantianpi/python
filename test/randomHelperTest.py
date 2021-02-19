#!/usr/bin/env python
# coding=utf-8

import unittest
from common import randomHelper


class RandomHelperTest(unittest.TestCase):
    """随机数操作包测试类"""

    def setUp(self):
        """初始化测试环境"""
        print('------ini------')

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')

    def test(self):
        print('获取0到100之间的随机数')
        print(randomHelper.get_number_for_range(0, 100))
        print(randomHelper.get_number_for_range(0, 100))

        print('获取长度为5的数字随机码')
        print(randomHelper.get_number(5))
        print(randomHelper.get_number(5))

        print('获取长度为6的英文随机码')
        print(randomHelper.get_letters(6))
        print(randomHelper.get_letters(6))

        print('获取长度为6的数字与英文随机码')
        print(randomHelper.get_string(6))
        print(randomHelper.get_string(6))

        print('获取uuid')
        print(randomHelper.get_uuid())
        print(randomHelper.get_uuid())
if __name__ == '__main__':
    unittest.main()