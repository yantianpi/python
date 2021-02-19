#!/usr/bin/env python
# coding=utf-8

import unittest
from common import exceptHelper


class exceptHelperTest(unittest.TestCase):
    """异常堆栈信息操作包测试类"""

    def setUp(self):
        """初始化测试环境"""
        print('------ini------')

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')

    def test(self):
        print(exceptHelper.detailtrace())

if __name__ == '__main__':
    unittest.main()
