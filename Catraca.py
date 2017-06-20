class Catraca():

	estado = "fechada"

	def abrir(self):
		if(self.estado == "fechada"):
			self.estado = "aberta"
		else:
			raise JaAberta()


	def rodar():
		if(self.estado == "aberta"):
			self.estado = "fechada"
		else:
			raise JaFechada()

class JaAberta(Exception):
	pass

class JaFechada(Exception):
	pass


c = Catraca()

c.abrir()