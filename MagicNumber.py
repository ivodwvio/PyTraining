# MagicNumber.py

import random

max_tryes = 10

print('\nWelcome to Magic Number\nMenu')
print('1: Start')
print('2: Instructions')

choice = int(input('> '))

if choice == 1:
	lucky = random.randint(1, 1000)
	tryes = 0
	
	while tryes < max_tryes:
		n = int(input('Guess {}: '.format(tryes + 1)))
		if n == lucky:
			print('You are right!')
			break
		else:
			if n > lucky:
				print('Too high.')
			else:
				print('Too low.')
			tryes += 1
			tryesLeft = max_tryes - tryes
			if tryesLeft == 0:
				print('Sorry, you did not guess the number.')
				print('The number is', lucky)
			else:
				print('Tryes left:', tryesLeft)
		print()
elif choice == 2:
	print('The computer have a number between 1 and 1000.')
	print('You have to guess it. You have {} tryes.'.format(max_tryes))
