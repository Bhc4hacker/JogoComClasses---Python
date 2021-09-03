from colorama import Fore, init
init(autoreset=True)
from random import *

class Jogo:
	def inicio(self):
		print("Ola, seja bem vindo!!")
		print(Fore.GREEN + "=" * 20)
		print("1 - Facil")
		print("2 - Medio")
		print("3 - Dificil")
		print(Fore.GREEN + "=" * 15)

	def verify_dificuldade(self, opcao):
		if opcao == 1:
			init.facil()
		elif opcao == 2:
			pass
		else:
			init.dificil()

	def facil(self):
		global calc2

		valor1 = randint(1,10)
		valor2 = randint(1,10)

		lista = ['+','-','*', '/']
		sorteador = randint(3, 3)
		print(valor1, lista[sorteador], valor2)

		if sorteador == 0:
			calc2 = valor1 + valor2
		elif sorteador == 1:
			calc2 = valor1 - valor2
		elif sorteador == 2:
			calc2 = valor1 * valor2
		else:
			calc2 = round((valor1/valor2),2)

	def dificil(self):
		global calc2

		valor1 = randint(1,10)
		valor2 = randint(1,10)
		valor3 = randint(1,10)

		lista = ['+','-','*']
		sorteador = randint(0, 2)
		sorteador2 = randint(0,2)
		print(valor1, lista[sorteador], "(",valor2, lista[sorteador2], valor3,")")

		if sorteador == 0:
			if sorteador2 == 0:
				calc2 = valor1 + (valor2 + valor3)
			elif sorteador2 == 1:
				calc2 = valor1 + (valor2 - valor3)
			else:
				calc2 = valor1 + (valor2 * valor3)
		elif sorteador == 1:
			if sorteador2 == 0:
				calc2 = valor1 - (valor2 + valor3)
			elif sorteador2 == 1:
				calc2 = valor1 - (valor2 - valor3)
			else:
				calc2 = valor1 - (valor2 * valor3)
		else:
			if sorteador2 == 0:
				calc2 = valor1 * (valor2 + valor3)
			elif sorteador2 == 1:
				calc2 = valor1 * (valor2 - valor3)
			else:
				calc2 = valor1 * (valor2 * valor3)

	def resultado(self, respostas):

		if respostas == calc2:
			print(Fore.GREEN + "Parabens voce acertou!!")
		else:
			print(Fore.RED + "Que pena voce errou :(")


init = Jogo()
init.inicio()
opcao = float(input())
init.verify_dificuldade(opcao)
respostas = float(input())
init.resultado(respostas)
