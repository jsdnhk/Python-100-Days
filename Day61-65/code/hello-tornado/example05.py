"""
example05.py - 異步請求的例子
"""
import aiohttp
import json
import os

import tornado.gen
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.httpclient
from tornado.options import define, options, parse_command_line

define('port', default=8888, type=int)

# 請求天行數據提供的API數據接口
REQ_URL = 'http://api.tianapi.com/guonei/'
# 在天行數據網站註冊後可以獲得API_KEY
API_KEY = 'your_personal_api_key'


class MainHandler(tornado.web.RequestHandler):
    """自定義請求處理器"""

    async def get(self):
        async with aiohttp.ClientSession() as session:
            resp = await session.get(f'{REQ_URL}?key={API_KEY}')
            json_str = await resp.text()
            print(json_str)
            newslist = json.loads(json_str)['newslist']
            self.render('news.html', newslist=newslist)


def main():
    """主函數"""
    parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', MainHandler), ],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
