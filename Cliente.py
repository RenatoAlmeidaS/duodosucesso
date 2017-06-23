import socket
import os
import linecache

def ler_porta(id):

	arq = open('portas', 'r')
	porta = int(linecache.getline('portas', id))
	arq.close()
	return porta

def escolher_catraca():
	a = int(raw_input('Em qual RU quer entrar:		--Digite "-1" para sair | "1" para RU 1 | "2" para RU 2 | "3" para RU 3--\n'))
	while (a<>1 and a<>2 and a<>3 and a<>-1):
		os.system("clear")
		a = int(raw_input('Resposta inválida, tente novamente:		--Digite "-1" para sair | "1" para RU 1 | "2" para RU 2 | "3" para RU 3--\n'))
	print ('Conectado a catraca: ' + str(a) + '		--Digite "exit" para sair--\n')
	return a

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while (True):
	try:
		dest = ('localhost', ler_porta(4))
		tcp.connect(dest)
		pass
	except Exception as e:
		print("Erro: {}".format(e))
		raw_input ('pressione qualqer tecla para continuar...\n')

	os.system('clear')
	catraca = escolher_catraca()
	while True:
		msg = raw_input()
		if (msg == 'exit'):
			os.system("clear")
			tcp.send('exitx')
			catraca = escolher_catraca()
			continue
		msg = msg + str(catraca)
		tcp.send (msg)
		print 'Catraca', catraca, 'respondeu', tcp.recv(1024)
	tcp.close()
	break