#!/usr/bin/python

import socket, time, sys, requests, urllib.request

#creo el socket object

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
        #establece la conexion
        conn, addr = serversocket.accept()
        print("Establecimos conexion con %s." % str(addr))
        print("El valor de conn es %s." % str(conn.getsockname()))

        my_get = urllib.request.urlopen("http://example.com/")
        request = conn.recv(9999)
        #print(("Request value and length {} \n {}.").format(request.decode(), len(request)))

        #import code
        #code.interact(local=locals())

        #print("Read: ", my_get.read(300).decode('utf-8'))

        conn.sendall(b'HTTP/1.0 200 OK\n')
        conn.sendall(b'Content-Type: text/html\n')
        conn.sendall(b'\r\n')
        conn.sendall(b'xxxxxxxxx')
        conn.sendall(b'<html><body>asdasd</body></html>')

        conn.close()

    except KeyboardInterrupt:
        print("\r\n")
        print("Socket cerrado a pedido del cliente.")
        sys.exit() #aca no pones conn.close() porque no estaria definido conn en algunos casos
    except Exception as e:
        print(e)

