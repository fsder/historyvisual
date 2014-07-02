import tornado.web
from tornado.httpclient import AsyncHTTPClient

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("index.html")

        self.flush()
        self.finish()

    # def _callback(self, response):
    #     self.write(response.body)
    #     self.finish()

settings = {
    "debug": True,
}

class NewsHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("news.html")
        self.flush()
        self.finish()

# application should be an instance of `tornado.web.Application`,
# and don't wrap it with `sae.create_wsgi_app`
application = tornado.web.Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
