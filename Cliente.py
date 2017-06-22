import socket
import os
import linecache

def ler_porta(id):

	arq = open('portas', 'r')
	porta = int(linecache.getline('portas', id))
	arq.close()
	print(porta)
	return porta
def escolher_catraca():
	return int(raw_input('Em qual RU quer entrar:\n'))
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	dest = ('localhost', ler_porta(escolher_catraca()))
	tcp.connect(dest)
	pass
except Exception as e:
	raw_input ('Erro, pressione qualqer tecla para continuar...\n')

os.system('clear')
print('Digite "exit" para sair')
msg = raw_input()
#con, cliente = tcp.accept()

while msg <> 'exit':

    tcp.send (msg)
    msg = raw_input()

tcp.close()