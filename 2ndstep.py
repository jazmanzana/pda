#!/usr/bin/python

import socket, sys, urllib

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = 8080 # si pones un puerto menor al 1024 tenes que correr el script como root


# para evitar el address already in use: el puerto se libera y se reusa
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#hago el bind para que se quede escuchando en el puerto que yo le digo
serversocket.bind((host, port))
serversocket.listen() #maximum number of queued connections 0-5: BACKLOG


while True:
    try:
        print("Esperando conexiones. Para terminar presione CRTL-C.")
        conn, addr = serversocket.accept()
        print("Establecimos conexion con %s." % str(addr))
        print("El valor de conn es %s." % str(conn.getsockname()))


        my_get = urllib.request.urlopen("http://example.com/")
        my_read_get = my_get.read()
        request = conn.recv(9999)

        #escribir funcion para volver a generar esta linea (!)
        print ("msg: ", my_get.msg)
        print ("version: ", my_get.version)
        print ("status: ", my_get.status)

        conn.sendall(b'HTTP/1.0 200 OK\n') # para suplantar esta (!)
        conn.sendall(bytes(my_get.headers))
        conn.sendall(b'\r\n')
        conn.sendall(my_read_get)

        conn.close()

    except KeyboardInterrupt:
        print("\r\n")
        print("Socket cerrado a pedido del cliente.")
        sys.exit()
    except Exception as e:
        print(e)

