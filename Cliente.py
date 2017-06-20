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

	PORT = ler_porta()				# Porta que o Servidor esta
	HOST = '127.0.0.1'				# Endereco IP do Servidor

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (HOST, PORT)

	try:
		tcp.connect(dest)
		pass
	except Exception as e:
		raw_input ("Falha no engano! Aperte uma tecla para tentar novamente!\n")
		continue
	os.system("clear")
	msg = raw_input()
	con, cliente = tcp.accept()

	while msg <> 'exit':

	    tcp.send (msg)
	    msg = raw_input()
		msg2 = con.recv(1024)
		if not msg2: break
		print (msg2)

	tcp.close()
	
	if msg == 'exit':
		break