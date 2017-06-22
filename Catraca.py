class Catraca():

	def __init__(self):
		self.estado = "fechada"

	def abrir(self):
		if(self.estado == "fechada"):
			self.estado = "aberta"
		else:
			raise JaAberta()


	def rodar(self):
		if(self.estado == "aberta"):
			self.estado = "fechada"
		else:
			raise JaFechada()

	def get_estado(self):
		return self.estado

class JaAberta(Exception):
	pass

class JaFechada(Exception):
	pass