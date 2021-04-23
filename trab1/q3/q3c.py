from time import sleep
import threading as td

class Conta:
	in_use = False
	historico = []
	def __init__ (self, saldo = 0):
		self.saldo = saldo

	def depositar(self, valor = 0, pessoa = 'Anonimo'):
		if not self.in_use and valor >= 0:
			self.in_use=True
			self.saldo += valor
			self.in_use = False
			print(f'Foi depositado: {valor} por: {pessoa} | saldo da conta: {self.saldo}')
			self.historico.append((pessoa,'deposito', valor, self.saldo))
			confirmation = True
		else:
			print(f'Aguarde, a conta está sendo usada')
			confirmation = False
		return confirmation

	def sacar(self, valor = 0, pessoa = 'Anonimo'):
		if (not self.in_use) and (self.saldo - valor) >= 0:
			self.in_use = True
			self.saldo -= valor
			self.in_use = False
			self.historico.append((pessoa,'saque', valor, self.saldo))
			confirmation = True
			print(f'Foi sacado: {valor} por: {pessoa} | saldo da conta: {self.saldo}')
		else:
			print(f'Aguarde, a conta está sendo usada')
			confirmation = False
		return confirmation

	def show_historico(self):
		for event in self.historico:
			print(event)


class Cliente:

	def __init__(self, nome):
		self.nome = nome

	def try_sacar(self, conta, valor = 0, n_max_tries = 1):
		while n_max_tries:
			if conta.sacar(valor, self.name):
				break

			sleep(4)

	def try_depositar(self, conta, valor = 0, n_max_tries = 1):
		while n_max_tries:
			if conta.depositar(valor, self.name):
				break
				
			sleep(4)

	def sequencia_de_operacoes(self, conta, valores, n_max_tries)
		x, y = valores
		try_sacar(conta, x, n_max_tries)
		try_depositar(conta, y, n_max_tries)



# c1 = Conta(200)
# c1.depositar(50, 'andre')
# c1.sacar(25,'joao')
# c1.sacar(17,'bolsonaro')
# c1.depositar(13, 'lula')
# c1.sacar(17,'lula')
# c1.show_historico()

