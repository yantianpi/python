#!/usr/bin/env python
# coding=utf-8

import unittest
from common import mailHelper, exceptHelper


class MailHelperTest(unittest.TestCase):
    """邮件操作包测试类"""

    def setUp(self):
        """初始化测试环境"""
        print('------ini------')

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')

    def test(self):
        mailHelper.send_mail('test', 'test', ['peteryan@meikaitech.com'])
        except_info = exceptHelper.detailtrace()
        mailHelper.send_error_mail('出现异常，堆栈信息：' + except_info)


if __name__ == '__main__':
    unittest.main()