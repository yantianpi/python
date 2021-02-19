#!/usr/bin/python
#coding: utf-8

from io import BytesIO
from bottle import get, response
from common import verifyHelper, logHelper, webHelper

@get('/api/verify/')
def get_verify():
    """生成验证码图片"""
    try:
        # 获取生成验证码图片与验证码
        code_img, verify_code = verifyHelper.create_verify_code()

        # 将字符串转化成大写保存到session中
        s = webHelper.get_session()
        s['verify_code'] = verify_code.upper()
        s.save()

        # 输出图片流
        buffer = BytesIO()
        code_img.save(buffer, "jpeg")
        code_img.close()
        response.set_header('Content-Type', 'image/jpg')
        return buffer.getvalue()
    except Exception as e:
        logHelper.error(str(e.args))