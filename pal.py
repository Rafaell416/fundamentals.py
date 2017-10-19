# -*- coding: utf-8 -*-


def palindrome(word):
	new = word[::-1]
	if word == new:
		print('{} es un plindromo.'.format(word))
	else:
		print('NO es un palindromo.')
	

if __name__ == '__main__':
   	word = str(input('Escribe una palabra: '))
   	palindrome(word)

