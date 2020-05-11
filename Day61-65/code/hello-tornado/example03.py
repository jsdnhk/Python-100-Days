"""
example03.py - RequestHandler解析
"""
import os
import re

import tornado.ioloop
import tornado.web

from tornado.options import define, options, parse_command_line


# 定義默認端口
define('port', default=8000, type=int)

users = {}


class User(object):
    """用戶"""

    def __init__(self, nickname, gender, birthday):
        self.nickname = nickname
        self.gender = gender
        self.birthday = birthday


class MainHandler(tornado.web.RequestHandler):
    """自定義請求處理器"""

    def get(self):
        # 從Cookie中讀取用戶暱稱
        nickname = self.get_cookie('nickname')
        if nickname in users:
            self.render('userinfo.html', user=users[nickname])
        else:
            self.render('userform.html', hint='請填寫個人信息')


class UserHandler(tornado.web.RequestHandler):
    """自定義請求處理器"""

    def post(self):
        # 從表單參數中讀取用戶暱稱、性別和生日信息
        nickname = self.get_body_argument('nickname').strip()
        gender = self.get_body_argument('gender')
        birthday = self.get_body_argument('birthday')
        # 檢查用戶暱稱是否有效
        if not re.fullmatch(r'\w{6,20}', nickname):
            self.render('userform.html', hint='請輸入有效的暱稱')
        elif nickname in users:
            self.render('userform.html', hint='暱稱已經被使用過')
        else:
            users[nickname] = User(nickname, gender, birthday)
            # 將用戶暱稱寫入Cookie並設置有效期爲7天
            self.set_cookie('nickname', nickname, expires_days=7)
            self.render('userinfo.html', user=users[nickname])


def main():
    """主函數"""
    parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/', MainHandler),
            (r'/register', UserHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
