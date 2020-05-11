"""
example01.py - 五分鐘上手Tornado
"""
import tornado.ioloop
import tornado.web

from tornado.options import define, options, parse_command_line

# 定義默認端口
define('port', default=8000, type=int)


class MainHandler(tornado.web.RequestHandler):
    """自定義請求處理器"""

    def get(self):
        # 向客戶端（瀏覽器）寫入內容
        self.write('<h1>Hello, world!</h1>')


def main():
    """主函數"""
    # 解析命令行參數，例如：
    # python example01.py --port 8888
    parse_command_line()
    # 創建了Tornado框架中Application類的實例並指定handlers參數
    # Application實例代表了我們的Web應用，handlers代表了路由解析
    app = tornado.web.Application(handlers=[(r'/', MainHandler), ])
    # 指定了監聽HTTP請求的TCP端口（默認8000，也可以通過命令行參數指定）
    app.listen(options.port)
    # 獲取Tornado框架的IOLoop實例並啓動它（默認啓動asyncio的事件循環）
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
