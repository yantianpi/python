#!/usr/bin/env python
# coding=utf-8

import logging
import logging.handlers
import traceback

from common import mailHelper, exceptHelper


def info(content):
    """记录日志信息"""
    if content:
        logging.info(content)

def error(content = '', is_send_mail = True):
    """记录错误日志信息"""
    if traceback:
        content = content + '\n' + traceback.format_exc() + '\n'
    # 获取程序当前运行的堆栈信息
    detailtrace = exceptHelper.detailtrace()
    content = content + '程序调用堆栈的日志：' + detailtrace + '\n'

    logging.error(content)

    # 发送邮件通知相关人员
    if is_send_mail:
        info = mailHelper.send_error_mail(context=content)
        if info: logging.info(info)


