from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
import sys

def fetch_future_asynchronicly():
    try:
        http_client = AsyncHTTPClient()
        my_future = Future()
        fetch_future = http_client.fetch("http://127.0.0.1:8888")
        fetch_future.add_done_callback(
            lambda f: my_future.set_result(f.result()))
        return my_future #porque es python3
    except Exception as e:
        print ("Error: %s" % e)

count = 0
while True:
    try:
        response = IOLoop.current().run_sync(fetch_future_asynchronicly)
        count += 1
        print ("Count goes {}.".format(count))
    except KeyboardInterrupt:
        print ("\r\n")
        print ("Cerrando a pedido tuyo.")
        sys.exit()
    except Exception as e:
        print ("Error: %s" % e)

#run_sync toma la funcion, no la tenes que llamar desde ahi

# try:
#     response = AsyncHTTPClient().fetch("127.0.0.1:8888")
#     print("llegue aca")
#     if response.exception():
#         print ("Response exception: %s " % response.exc_info())
#     else:
#         print(response.result())
# except Exception as e:
#     print("Error: ", e)

