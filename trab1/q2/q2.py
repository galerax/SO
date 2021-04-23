import time
import threading
import random as rd


class crianca:
	tempo = 3
	com_bola = False
	esperando = True
	def __init__(self, nome, habilidade):
		self.nome = nome
		self.habilidade = habilidade
		self.priority = habilidade/100

	def jogando(self, bola_sobrando):
		while True:
			if bola_sobrando.state == True:
				bola_sobrando.state = False
				self.com_bola = True
				print(f'{self.nome}: Peguei! \n')
				time.sleep(self.tempo)
				bola_sobrando.state = True
				self.com_bola = False
				print(f'{self.nome}: Soltei! \n')
			else:
				self.esperando = True
			self.test_priority()

	def test_priority(self):
		time.sleep(1-self.priority)


class bola:
	state= False


criancas = [crianca(nome, rd.randint(0,100)) for nome in range(100)]

bola = bola()
threads = []

for c in criancas:
	t = threading.Thread(target = c.jogando, kwargs=dict(bola_sobrando=bola))
	t.start()
	threads.append(t)

# começando a brincadeira
bola.state = True
