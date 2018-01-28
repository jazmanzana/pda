#!/usr/bin/python

import socket, time, sys

#creo el socket object

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#los pongo aca mejor asi es mas facil el setting
host = "" #vacio equivale a localhost
# si pones un puerto menor al 1024 tenes que correr el script como root
port = 8080
print("My host is %s. " % str(host))
print("My port is %s. " % str(port))

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

        request = conn.recv(99999)  # sin esto no hay display en el client (necesitas recibir el GET de su parte)
        print(("Request value and length {} \n {}.").format(request.decode(), len(request)))


        conn.sendall(b'HTTP/1.0 200 OK\n') #convencion
        conn.sendall(b'Content-Type: text/html\n')
        conn.sendall(b'\n')  # separa header y body
        algo = time.time()
        conn.sendall(b"<html><body><h1>Hey you guys!</h1></body></html>")
        # uso sendall para no tener que chequear si quedan cosas por enviar o no
        conn.close()

    except KeyboardInterrupt:
        print("\r\n")
        print("Socket cerrado a pedido del cliente.")
        sys.exit() #aca no pones conn.close() porque no estaria definido conn en algunos casos
    conn.close()