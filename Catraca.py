class Catraca():
	livre = True
	def __init__(self):
		self.estado = "fechada"

	def abrir(self):
		if(self.estado == "fechada"):
			self.estado = "aberta"
			self.livre = False
		else:
			raise JaAberta()


	def rodar(self):
		if(self.estado == "aberta"):
			self.estado = "fechada"
			self.livre = True
		else:
			raise JaFechada()

	def get_estado(self):
		return self.livre

class JaAberta(Exception):
	pass

class JaFechada(Exception):
	pass