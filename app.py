import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/yhl", tornado.web.RedirectHandler, {"url": "/shop/index.html"}),
        (r"/yhl/", tornado.web.RedirectHandler, {"url": "/shop/index.html"}),
        (r"/yhl/(.*)", tornado.web.StaticFileHandler, {"path": "dist"}),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "dist/css"}),
        (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "dist/js"}),
        (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "dist/img"}),
        (r"/fonts/(.*)", tornado.web.StaticFileHandler, {"path": "dist/fonts"})
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(port=8888, address='0.0.0.0')
    tornado.ioloop.IOLoop.current().start()
