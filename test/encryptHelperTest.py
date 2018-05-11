#!/usr/bin/env python
# coding=utf-8

import unittest
from common import encryptHelper


class encryptHelperTest(unittest.TestCase):
    """加密操作包测试类"""

    def setUp(self):
        """初始化测试环境"""
        print('------ini------')

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')

    def test(self):
        result = encryptHelper.md5(3)
        print(result)
        self.assertEqual(result, 'eccbc87e4b5ce2fe28308fd9f2a7baf3')

        result = encryptHelper.md5('3')
        print(result)
        self.assertEqual(result, 'eccbc87e4b5ce2fe28308fd9f2a7baf3')

        result = encryptHelper.md5(b'3')
        print(result)
        self.assertEqual(result, 'eccbc87e4b5ce2fe28308fd9f2a7baf3')

        result = encryptHelper.md5('123456').upper()
        print(result)
if __name__ == '__main__':
    unittest.main()
