#!/usr/bin/env python
# coding=utf-8
import logging
import os
import unittest
from common import logHelper
class LogHelperTest(unittest.TestCase):
    """日志操作包测试类"""
    def setUp(self):
        """初始化测试环境"""
        print('------ini------')
        # 获取本脚本所在的上级路径（因为logHelper_text.py是在test目录下面，并不在根目录，而我们想将日志都记录在根据目录下的log目录里，所以需要获取test的上级目录）
        program_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # 初始化日志目录
        log_path = os.path.join(program_path, 'log')
        # 当日志目录不存在时创建日志目录
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        # 定义日志输出格式
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            filename="%s/info.log" % log_path,
                            filemode='a')
    def tearDown(self):
        """清理测试环境"""
        print('------clear------')
    def test(self):
        logHelper.info('记录代码执行的相关记录或信息')
        try:
            result = '0' / 10
        except Exception as e:
            logHelper.error('出现异常：' + str(e.args))
if __name__ == '__main__':
    unittest.main()