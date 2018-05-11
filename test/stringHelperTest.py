#!/usr/bin/env python
# coding=utf-8

import unittest
from common import stringHelper


class StringHelperTest(unittest.TestCase):
    """字符串操作包测试类"""

    def setUp(self):
        """初始化测试环境"""
        print('------ini------')

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')

    def test_is_email(self):
        self.assertEqual(stringHelper.is_email('aaaaa'), False)
        self.assertEqual(stringHelper.is_email('aaaa@xxx.com'), True)
        self.assertEqual(stringHelper.is_email('xxx@xxx.com.xx'), True)

    def test_is_phone(self):
        self.assertEqual(stringHelper.is_phone('aaaaa'), False)
        self.assertEqual(stringHelper.is_phone('12345678'), False)
        self.assertEqual(stringHelper.is_phone('01012345678'), True)
        self.assertEqual(stringHelper.is_phone('010-123456'), False)
        self.assertEqual(stringHelper.is_phone('010-12345678'), True)
        self.assertEqual(stringHelper.is_phone('010 12345678'), True)
        self.assertEqual(stringHelper.is_phone('0757 12345678'), True)

    def test_is_mobile(self):
        self.assertEqual(stringHelper.is_mobile('aaaaa'), False)
        self.assertEqual(stringHelper.is_mobile('123456789'), False)
        self.assertEqual(stringHelper.is_mobile('13012345678'), True)
        self.assertEqual(stringHelper.is_mobile('14012345678'), False)

    def test_is_letters(self):
        self.assertEqual(stringHelper.is_letters('123456'), False)
        self.assertEqual(stringHelper.is_letters('1ds2f12sdf'), False)
        self.assertEqual(stringHelper.is_letters('absbdsf'), True)
        self.assertEqual(stringHelper.is_letters('ADdfFSds'), True)

    def test_is_idcard(self):
        self.assertEqual(stringHelper.is_idcard('123456789'), False)
        self.assertEqual(stringHelper.is_idcard('aaaaaaaaa'), False)
        self.assertEqual(stringHelper.is_idcard('340223190008210470'), False)
        self.assertEqual(stringHelper.is_idcard('34022319000821047X'), True)

    def test_filter_str(self):
        print(stringHelper.filter_str('aaa'))
        print(stringHelper.filter_str('aaa<>&\''))
        print(stringHelper.filter_str('aaa<|>|&|%|~|^|;|\''))

    def test_filter_tags(self):
        print(stringHelper.filter_tags('<html><body><b>aaa</b></body></html>'))

    def test_string(self):
        print(stringHelper.string(-1))
        print(stringHelper.string({'test': 'abc'}))
        print(stringHelper.string(''))
        print(stringHelper.string('aaa'))
        print(stringHelper.string('', True))

    def test_cut_str(self):
        print(stringHelper.cut_str('', 5))
        print(stringHelper.cut_str('aaa', 5))
        print(stringHelper.cut_str('将字符串截取指定长度', 5))
        print(stringHelper.cut_str('aa将字符串截取指定长度', 5))

    def test_clear_xss(self):
        print('-----test_clear_xss------')
        print(stringHelper.clear_xss('<script src="javascript:alert(1);">abc</script>'))
        print(stringHelper.clear_xss('<iframe src="javascript:alert(1);">abc</iframe>'))
        print(stringHelper.clear_xss(
            '<div style="width:0;height:0;background:url(javascript:document.body.onload = function(){alert(/XSS/);};">div</div>'))
        print(stringHelper.clear_xss('<img src = "#"/**/onerror = alert(/XSS/)>'))
        print(stringHelper.clear_xss('<img src = j ava script:al er t(/XSS/)>'))
        print(stringHelper.clear_xss("""<img src = j
        ava script :a ler t(/xss/)>"""))
        print(stringHelper.clear_xss('<img src="javacript:alert(\'abc\')"></img>'))
        print(stringHelper.clear_xss('<img src="https://www.baidu.com/img/baidu_jgylogo3.gif"></img>'))
        print(stringHelper.clear_xss('<p src="javascript:alert(1);">abc</p>'))
        print(stringHelper.clear_xss("""<input type="text" value="琅琊榜" onclick="javascript:alert('handsome boy')">"""))
        print(stringHelper.clear_xss('<p onclick="javascript:alert("handsome boy")>abc</p>'))
        print(stringHelper.clear_xss('<a href="javascript:alert(1);">abc</a>'))
        print(stringHelper.clear_xss('<a href="/api/">abc</a>'))
        print(stringHelper.clear_xss('<a href="http://www.baidu.com">abc</a>'))
        print(stringHelper.clear_xss('<marquee onstart="alert(/XSS/)">文字</marquee>'))
        print(stringHelper.clear_xss('<div style="" onmouseenter="alert(/XSS/)">文字</div>'))
        print(stringHelper.clear_xss('<li style = "TEST:e-xpression(alert(/XSS/))"></li>'))
        print(stringHelper.clear_xss('<input id = 1 type = "text" value="" <script>alert(/XSS/)</script>"/>'))
        print(stringHelper.clear_xss('<base href="http://www.labsecurity.org"/>'))
        print(stringHelper.clear_xss('<div id="x">alert%28document.cookie%29%3B</div>'))
        print(stringHelper.clear_xss('<limited_xss_point>eval(unescape(x.innerHTML));</limited_xss_point>'))


if __name__ == '__main__':
    unittest.main()