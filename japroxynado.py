import tornado.ioloop, tornado.web, urllib.request

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        my_get = urllib.request.urlopen("http://www.python.org/")
        my_get_content = my_get.read()
        self.write(my_get_content)
        print("my get content is: ", my_get_content)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
