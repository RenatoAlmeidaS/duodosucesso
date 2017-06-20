import socket


HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = ler_porta()            # Porta que o Servidor esta



tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)
msg = raw_input()

while msg <> '\x18':

    tcp.send (msg)
    msg = raw_input()

tcp.close()

def ler_porta():

		porta = 0
		escolha = 0

		while (escolha < 1 or escolha > 2):	
			os.system("clear")	
			escolha = raw_input("Porta servidor:\n1-Padrao\n2-Digitar porta\n")

		if (escolha == 1):
			porta = 5555
		else:
			porta = raw_input("Digite a porta:\n")

		return porta