# -*- coding: utf-8 -*-
import random


def run():
	number_found = False
	random_number = random.randint(0, 20)

	while not number_found:
		number = int(input('Intenta un numero: '))

		if number == random_number:
			print('Felicidades ya lo encontrate')
			number_found = True
		elif number > random_number:
			print('Es numero es mas pequeño.')
		else:
			print('El numero es más grande')
   
if __name__ == '__main__':
   	run()
