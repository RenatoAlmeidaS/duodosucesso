import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = ('localhost', 56000)
tcp.connect(dest)

msg = 'rola'
while msg <> 'exit':

    tcp.send (msg)
    msg = raw_input()
    data = tcp.recv(1024)
    print (data)

    #tcp.listen(1)
    #con, servidor = tcp.accept()
    #msg2 = con.recv(1024)
    #print msg2 + servidor
