import socket
import os

def ler_porta():

	porta = 0
	escolha = 0

	while (escolha < 1 or escolha > 2):	
		os.system("clear")	
		escolha = input("Porta servidor:\n1-Padrao\n2-Digitar porta\n")

	if (escolha == 1):
		porta = 5555
	else:
		porta = input("Digite a porta:\n")

	return porta

while (True):

	HOST = '127.0.0.1'				# Endereco IP do Servidor

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		dest = (HOST, ler_porta())
		tcp.connect(dest)
		pass
	except Exception as e:
		raw_input ("Falha no engano! Aperte uma tecla para tentar novamente!\n")
		continue
	os.system("clear")
	msg = raw_input()


	while msg <> 'exit':

	    tcp.send (msg)
	    msg = raw_input()

	tcp.close()
	
	if msg == 'exit':
		break