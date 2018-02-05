import tornado.ioloop, tornado.web, urllib.request, signal, logging, tornado.options, time
import tornado.websocket
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

# +++++++++++ #

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        my_get = urllib.request.urlopen("https://www.mercadolibre.com.ar")
        print("this is my_get: ", dir(my_get))
        my_get_content = my_get.read()
        self.write(my_get_content)
        print("my get url: ", my_get.url)
        print("my get reason: ", my_get.reason)
        print("my get status: ", my_get.status)
        print("my get flush: ", dir(my_get.flush))
        print("my get header: ", my_get.headers)
        print("my get info: ", my_get.info)

class SitesHandler(tornado.web.RequestHandler):
    def get(self):
        my_get = urllib.request.urlopen("https://www.mercadolibre.com.ar/sites")
        print("this is my_get: ", dir(my_get))
        my_get_content = my_get.read()
        self.write(my_get_content)

application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/sites", SitesHandler),
    ])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    signal.signal(signal.SIGINT, signal_handler) # ctrl + c
    a = application.listen(8888)
    print ("this is a: ", dir(a))
    #explain PeriodicCallback
    tornado.ioloop.PeriodicCallback(try_exit, 100).start() # ctrl + c
    my_ioloop = tornado.ioloop.IOLoop.current()
    print("this is current: ", dir(my_ioloop))
    my_ioloop.start()



#
# class Client:
#     RECEIVING = 0
#     SENDING = 1
#     FINISHED = 2
#
#     def __init__(self, connection, addr):
#         self.connection = connection
#         self.addr = addr
#         self.state = Client.RECEIVING
#         self.received = bytes()
#         self.to_send = b'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n<html>Server V5</html>\r\n' #no me gusta
#         self.bytes_sent = 0
#         self.conection_time = time.localtime()
#
# clients = {}
