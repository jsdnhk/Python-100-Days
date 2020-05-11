"""
example02.py - 路由解析
"""
import os
import random

import tornado.ioloop
import tornado.web

from tornado.options import define, options, parse_command_line


# 定義默認端口
define('port', default=8000, type=int)


class SayingHandler(tornado.web.RequestHandler):
    """自定義請求處理器"""

    def get(self):
        sayings = [
            '世上沒有絕望的處境，只有對處境絕望的人',
            '人生的道路在態度的岔口一分爲二，從此通向成功或失敗',
            '所謂措手不及，不是說沒有時間準備，而是有時間的時候沒有準備',
            '那些你認爲不靠譜的人生裏，充滿你沒有勇氣做的事',
            '在自己喜歡的時間裏，按照自己喜歡的方式，去做自己喜歡做的事，這便是自由',
            '有些人不屬於自己，但是遇見了也彌足珍貴'
        ]
        # 渲染index.html模板頁
        self.render('index.html', message=random.choice(sayings))


class WeatherHandler(tornado.web.RequestHandler):
    """自定義請求處理器"""

    def get(self, city):
        # Tornado框架會自動處理百分號編碼的問題
        weathers = {
            '北京': {'temperature': '-4~4', 'pollution': '195 中度污染'},
            '成都': {'temperature': '3~9', 'pollution': '53 良'},
            '深圳': {'temperature': '20~25', 'pollution': '25 優'},
            '廣州': {'temperature': '18~23', 'pollution': '56 良'},
            '上海': {'temperature': '6~8', 'pollution': '65 良'}
        }
        if city in weathers:
            self.render('weather.html', city=city, weather=weathers[city])
        else:
            self.render('index.html', message=f'沒有{city}的天氣信息')


class ErrorHandler(tornado.web.RequestHandler):
    """自定義請求處理器"""

    def get(self):
        # 重定向到指定的路徑
        self.redirect('/saying')


def main():
    """主函數"""
    parse_command_line()
    app = tornado.web.Application(
        # handlers是按列表中的順序依次進行匹配的
        handlers=[
            (r'/saying/?', SayingHandler),
            (r'/weather/([^/]{2,})/?', WeatherHandler),
            (r'/.+', ErrorHandler),
        ],
        # 通過template_path參數設置模板頁的路徑
        template_path=os.path.join(os.path.dirname(__file__), 'templates')
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
