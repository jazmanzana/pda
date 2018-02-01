#!/usr/bin/python

import socket, sys, urllib.request
from tornado.options import define, options

define("host_and_port", default=8080, help="Run on the given ip and port.")

def response_first_line(version, status, message):
    return ('HTTP/{}.{} {} {}\r\n').format(version[:1], version[1:], status, message)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = 8080 # si pones un puerto menor al 1024 tenes que correr el script como root



# para evitar el address already in use: el puerto se libera y se reusa
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#hago el bind para que se quede escuchando en el puerto que yo le digo
serversocket.bind((host, port))
serversocket.listen(5) #maximum number of queued connections 0-5: BACKLOG


while True:
    try:
        print("Esperando conexiones. Para terminar presione CRTL-C.")
        conn, addr = serversocket.accept()
        print("Establecimos conexion con %s." % str(addr))
        print("El valor de conn es %s." % str(conn.getsockname()))


        my_get = urllib.request.urlopen("http://www.python.org/")
        my_get_content = my_get.read()
        request = conn.recv(9999)

        conn.sendall(response_first_line(str(my_get.version),my_get.status,my_get.msg).encode()+bytes(my_get.headers)+b'\r\n\r\n')
        conn.sendall(my_get_content)

        conn.close()

    except KeyboardInterrupt:
        print("\r\n")
        print("Socket cerrado a pedido del cliente.")
        sys.exit()
    except Exception as e:
        print(e)


