#!/usr/bin/env python
# coding=utf-8

from bottle import get, put
from common import dbHelper, webHelper, stringHelper

@get('/api/about/')
def callback():
    """
    获取指定记录
    """
    sql = """select * from infomation where id = '1'"""
    # 读取记录
    result = dbHelper.read(sql)
    if result:
        # 直接输出json
        return webHelper.return_msg(0, '成功', result[0])
    else:
        return webHelper.return_msg(-1, "查询失败")


@put('/api/about/')
def callback():
   """
   修改记录
   """
   front_covet_img = webHelper.get_form('front_cover_img', '图片')
   content = webHelper.get_form('content', '内容', is_check_special_char=False)
   # 防sql注入攻击处理
   content = stringHelper.filter_str(content, "'")
   # 防xss攻击处理
   content = stringHelper.clear_xss(content)

   # 更新记录
   sql = """update infomation set front_cover_img=%s, content=%s where id='1'"""
   vars = (front_covet_img, content)
   # 写入数据库
   dbHelper.write(sql, vars)

   # 直接输出json
   return webHelper.return_msg(0, '成功')

