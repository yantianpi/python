#!/usr/bin/env python
# coding=utf-8

import datetime
import unittest
from common import convertHelper


class ConvertHelperTest(unittest.TestCase):
    """转换操作包测试类"""

    def setUp(self):
        """初始化测试环境"""
        print('------ini------')

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')

    def test_to_int(self):
        self.assertEqual(convertHelper.to_int('1'), 1)
        self.assertEqual(convertHelper.to_int('1.0'), 0)
        self.assertEqual(convertHelper.to_int('1a'), 0)
        self.assertEqual(convertHelper.to_int('aaa'), 0)
        self.assertEqual(convertHelper.to_int(''), 0)
        self.assertEqual(convertHelper.to_int(None), 0)
        self.assertEqual(convertHelper.to_int('-1'), -1)
        self.assertEqual(convertHelper.to_int(10), 10)
        self.assertEqual(convertHelper.to_int(-10), -10)

        self.assertEqual(convertHelper.to_int0('1'), 1)
        self.assertEqual(convertHelper.to_int0('1.0'), 0)
        self.assertEqual(convertHelper.to_int0('1a'), 0)
        self.assertEqual(convertHelper.to_int0('aaa'), 0)
        self.assertEqual(convertHelper.to_int0(''), 0)
        self.assertEqual(convertHelper.to_int0(None), 0)
        self.assertEqual(convertHelper.to_int0('-1'), 0)
        self.assertEqual(convertHelper.to_int0(10), 10)
        self.assertEqual(convertHelper.to_int0(-10), 0)

        self.assertEqual(convertHelper.to_int1('1'), 1)
        self.assertEqual(convertHelper.to_int1('1.0'), 1)
        self.assertEqual(convertHelper.to_int1('1a'), 1)
        self.assertEqual(convertHelper.to_int1('aaa'), 1)
        self.assertEqual(convertHelper.to_int1(''), 1)
        self.assertEqual(convertHelper.to_int1(None), 1)
        self.assertEqual(convertHelper.to_int1('-1'), 1)
        self.assertEqual(convertHelper.to_int1(10), 10)
        self.assertEqual(convertHelper.to_int1(-10), 1)

        self.assertEqual(convertHelper.to_datetime(None), None)
        self.assertEqual(convertHelper.to_datetime(''), None)
        self.assertEqual(convertHelper.to_datetime('xxx'), None)
        result = datetime.datetime(2017, 9, 1)
        self.assertEqual(convertHelper.to_datetime('2017-09-01'), result)
        result = datetime.datetime(2017, 9, 1, 11, 11)
        self.assertEqual(convertHelper.to_datetime('2017-09-01 11:11'), result)
        self.assertEqual(convertHelper.to_datetime('2017-09-0111:11'), None)
        result = datetime.datetime(2017, 9, 1, 11, 11, 11)
        self.assertEqual(convertHelper.to_datetime('2017-09-01 11:11:11'), result)
        result = datetime.datetime(2017, 9, 1, 11, 11, 11, 111000)
        self.assertEqual(convertHelper.to_datetime('2017-09-01 11:11:11.111'), result)


if __name__ == '__main__':
    unittest.main()