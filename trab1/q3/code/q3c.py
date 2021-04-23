from time import sleep
import threading as td


class Conta:
	in_use = True

	def __init__(self, saldo = 0, nome = 'NOT NAMED'):
		self.saldo = saldo
		self.nome = nome
		self.historico = []

	def depositar(self, valor = 0, pessoa = 'Anonimo'):
		if valor >= 0:
			self.saldo += valor
			print(f'Foi depositado: {valor} por: {pessoa} | saldo da conta {self.nome}: {self.saldo} \n')
			self.historico.append((pessoa,'deposito', valor, self.saldo))
			confirmation = True
		else:
			print(f'Ocorreu um erro na operacao \n')
			confirmation = False
		sleep(1)
		return confirmation

	def sacar(self, valor = 0, pessoa = 'Anonimo'):
		if (self.saldo - valor) >= 0:
			self.saldo -= valor
			self.historico.append((pessoa,'saque', valor, self.saldo))
			confirmation = True
			print(f'Foi sacado: {valor} por: {pessoa} | saldo da conta {self.nome}: {self.saldo} \n')
		else:
			print(f'Ocorreu um erro na operacao \n')
			confirmation = False
		sleep(1)
		return confirmation

	def show_historico(self):
		for event in self.historico:
			print(event)


class Cliente:

	def __init__(self, nome):
		self.nome = nome

	def tentar_depositar(self, conta, valor = 0, n_max_tries = 1):
		while n_max_tries:
			sleep(2)
			if not conta.in_use:
				conta.in_use=True
				conta.depositar(valor, self.nome)
				conta.in_use= False
				break
			else:
				print(f'Cliente {self.nome} aguardando...')

	def tentar_sacar(self, conta, valor = 0, n_max_tries = 1):
		while n_max_tries:
			sleep(2)
			if not conta.in_use:
				conta.in_use=True
				conta.sacar(valor, self.nome)
				conta.in_use= False
				break
			else:
				print(f'Cliente {self.nome} aguardando...')

	
	def script(self, conta1, conta2, valores, max_tries):
		x, y = valores[0], valores[1]

		self.tentar_sacar(conta1, x, max_tries)		
		self.tentar_depositar(conta2, y, max_tries)


#Criando as entidades do programa
conta1 = Conta(500, 'A')
conta2 = Conta(900, 'B')
cliente1, cliente2 = Cliente('Joao'), Cliente('Andre')

#Definindo e iniciando as threads com uma função target
t1 = td.Thread(target=cliente1.script, kwargs=dict(conta1=conta1, conta2=conta2, valores = [200, 100], max_tries = 50))
t2 = td.Thread(target=cliente2.script, kwargs=dict(conta1=conta1, conta2=conta2, valores = [100, 200], max_tries = 50))

t1.start()
t2.start()

#Começando a brincadeira
conta1.in_use, conta2.in_use = False, False

#Esperando o retorno das threads
t1.join()
t2.join()

#Apresentando os resultados finais
print('\n\nLog Conta1')
conta1.show_historico()
print('------------------')
print('Log Conta2')
conta2.show_historico()
print(f'\nSALDO 1: {conta1.saldo}, SALDO2: {conta2.saldo}')
