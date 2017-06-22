import socket
import os
import sys

HOST = ''
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

orig = (HOST, 56000)
tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    pid = os.fork()
    if pid == 0:
        tcp.close()
        print 'Conectado por', cliente
        while True:
            msg = con.recv(1024)
            con.send(msg +  ' rola')
            if not msg: break
            print cliente, msg
        print 'Finalizando conexao do cliente', cliente
        con.close()
        sys.exit(0)
    else:
        con.close()