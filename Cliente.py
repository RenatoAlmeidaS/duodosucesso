import socket
import os
import linecache

def ler_porta(id):

	arq = open('portas', 'r')
	porta = int(linecache.getline('portas', id))
	arq.close()
	return porta

def escolher_catraca():
	return int(raw_input('Em qual RU quer entrar:\n'))

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
catraca = escolher_catraca()
while (True):

	try:
		dest = ('localhost', ler_porta(4))
		tcp.connect(dest)
		pass
	except Exception as e:
		print("Erro: {}".format(e))
		raw_input ('pressione qualqer tecla para continuar...\n')

	os.system('clear')
	print('Digite "exit" para sair')
	msg = raw_input() + str(catraca)

	while msg <> 'exit':

	    tcp.send (msg)
	    msg = raw_input() + str(catraca)

	tcp.send (msg)
	tcp.close()