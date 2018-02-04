import tornado.ioloop, tornado.web, urllib.request, signal, logging, tornado.options

# funciones para cerrar el server con ctrl+C y libreria signal (sin try... except...)
is_closing = False

def signal_handler(signal, frame): #convencion de signal
    global is_closing
    logging.info('Saliendo...')
    is_closing = True

def try_exit():
    global is_closing
    if is_closing:
        tornado.ioloop.IOLoop.instance().stop() #linea maestra
        logging.info('Server cerrado.')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        my_get = urllib.request.urlopen("http://www.google.com/")
        my_get_content = my_get.read()
        self.write(my_get_content)


application = tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    signal.signal(signal.SIGINT, signal_handler)
    application.listen(8888)
    #explain PeriodicCallback
    tornado.ioloop.PeriodicCallback(try_exit, 100).start()
    tornado.ioloop.IOLoop.instance().start() #instance vs current
