import socket
from Catraca import Catraca
import os
import linecache


mensagem = ""
catraca = Catraca()

def ler_porta(id):

	arq = open('portas', 'r')
	porta = int(linecache.getline('portas', id))
	arq.close()
	return porta

def tratar(mensagem):
	
	resposta = ""

	if(mensagem == "abrir"):
		try:
			catraca.abrir()
			resposta = "catraca aberta"
		except Exception as e:
			resposta = "catraca ja esta aberta"

	elif(mensagem =="estado"):
		resposta = catraca.get_estado()

	elif(mensagem == "rodar"):
		try:
			catraca.rodar()
			resposta = "catraca fechada"
		except Exception as e:
			resposta = "catraca ja esta fechada"
	else:
		resposta = "mensagem nao catalogada"

	return resposta


HOST = ''
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
id_catraca = 1
erro = True

while erro:
	try:
		orig = (HOST, ler_porta(id_catraca))
		tcp.bind(orig)
		erro = False
	except Exception as e:
		raw_input('Erro: {}\nDigite qualquer tecla para continuar...'.format(e))
		id_catraca += 1

tcp.listen(1)
os.system("clear")
while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    while True:
        msg = con.recv(1024)
        if (msg == 'exit'): 
        	break
        print cliente, tratar(msg)
    print 'Finalizando conexao do cliente', cliente
    con.close()
    break