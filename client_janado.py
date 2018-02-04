from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future
from tornado.ioloop import IOLoop

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

response = IOLoop.current().run_sync(fetch_future_asynchronicly)
#run_sync toma la funcion, no la tenes que llamar desde ahi
print("my response would be: %s" % response.body)

# try:
#     response = AsyncHTTPClient().fetch("127.0.0.1:8888")
#     print("llegue aca")
#     if response.exception():
#         print ("Response exception: %s " % response.exc_info())
#     else:
#         print(response.result())
# except Exception as e:
#     print("Error: ", e)

