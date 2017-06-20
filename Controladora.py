from Catraca import Catraca
import os

class Controller():

	mensagem = ""
	catraca = Catraca()




	
	def ler_porta(self):

		porta = 0
		escolha = 0

		while (escolha < 1 or escolha > 2):	
			os.system("clear")	
			escolha = input("Usar porta padrao ou outra:\n1-Padrao\n2-Digitar porta\n")

		if (escolha == 1):
			porta = 5555
		else:
			porta = input("Digite a porta:\n")

		return porta

	def tratar(mensagem):
		
		resposta = ""

		if(mensagem == "abrir"):
			try:
				catraca.abrir()
				resposta = "catraca aberta"
			except Exception as e:
				resposta = e.getMessage()

		elif(mensagem =="aberta?"):
			resposta = catraca.estado()

		else:
			resposta = "mensagem nao catalogada"

		return resposta

c = Controller()

print(c.ler_porta())