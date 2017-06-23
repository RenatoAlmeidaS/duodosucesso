import socket
import os
import sys
import linecache


def ler_porta(id):

	arq = open('portas', 'r')
	porta = int(linecache.getline('portas', id))
	arq.close()
	return porta

def tratar_mensagem(mensagem, id_catraca):
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = ("localhost", ler_porta(int(id_catraca)))
	print 'Enviando "', mensagem, '" para catraca ', id_catraca
	tcp.connect(dest)
	tcp.send (mensagem)
	resposta = tcp.recv(1024)
	print 'Resposta recebida da catraca', id_catraca,':' , resposta
	tcp.close()
	return resposta



rel_cli_cat = {1:0, 2:0, 3:0}
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
orig = ('', ler_porta(4))

tcp.bind(orig)
tcp.listen(3)

while True:

	con, cliente = tcp.accept()
	pid = os.fork()

	if pid == 0:
		#tcp.close()

		print 'Conectado ao Cliente ', cliente

		while True:
			msg = con.recv(1024)
			id_catraca = msg[-1]
			msg = msg[:-1]
			if msg == 'exit':
				break
			con.send(tratar_mensagem(msg, id_catraca))
		
		print 'Finalizando conexão com cliente', cliente
		con.close()
	
	else:
		con.close()