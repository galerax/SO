import threading
import time


class Saldo:
	def __init__(self, name, value):
		self.name = name
		self.value = value
		self.begin = False


def s1(saldo):
	while True:
		if saldo.begin:
			x = saldo.value
			# print("x: ",x)
			x = x-200
			saldo.value = x
			# print(f'depositado x : {saldo.value}')
			break

def s2(saldo):
	while True:
		if saldo.begin:
			y = saldo.value
			y = y-100
			# print("y: ",y)
			saldo.value = y
			# print(f'depositado y : {saldo.value}')
			break

def d1(saldo):
	while  True:
		if (saldo.begin):
			x = saldo.value
			x = x+100
			saldo.value = x
			break

def d2(saldo):
	while  True:
		if (saldo.begin):
			y = saldo.value
			y = y+200
			saldo.value = y
			break



saldo_a, saldo_b = Saldo("a", 500), Saldo("b", 900)



t1 = threading.Thread(target=s1, kwargs=dict(saldo=saldo_a))
t2 = threading.Thread(target=s2, kwargs=dict(saldo=saldo_a))

t1.start()
t2.start()

saldo_a.begin = True



t3 = threading.Thread(target=d1, kwargs=dict(saldo=saldo_b))
t4 = threading.Thread(target=d2, kwargs=dict(saldo=saldo_b))

t3.start()
t4.start()



saldo_b.start = True

time.sleep(1)
print(saldo_a.value, saldo_b.value)
