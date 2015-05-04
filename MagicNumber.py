# MagicNumber.py

import random
from Engine import program_cycle
from Engine import display_menu_title

MAX_VALUE = 100

def instructions():
	display_menu_title('Instructions', 30)
	print('The computer have a number between 0 and MAX_VALUE.')
	print('MAX_VALUE by default is 100. You can set it in Settings.')
	print('Your mission is to find the number.')

def statistics(numbers, lucky):
	display_menu_title('Statistics', 30)
	for n in range(len(numbers)):
		print('Try {} Number = {} Result = {}'.format(
				n + 1, numbers[n],
				'LOW' if numbers[n] < lucky
				else 'HIGH' if numbers[n] > lucky
				else 'EQUAL'))

def settings():
	display_menu_title('Settings', 25)
	answer = input('Do you want to change the MAX_VALUE?(y/n):')
	if answer == 'y':
		global MAX_VALUE
		MAX_VALUE = int(input('new value = '))
	elif answer == 'n':
		return
	else:
		print('Invalid answer.')

def new_game():
	low = 0
	high = MAX_VALUE
	lucky = random.randint(low, high)
	searching = True
	tryes = 0
	middle = round(high / 2)
	numbers = []

	display_menu_title('Game Start', 27)
	print('Help: start with MAX_VALUE / 2 =', middle)

	while searching:
		n = int(input('Guess {}: '.format(tryes + 1)))
		if n < 0:
			print('Number can\'t be negative.\n')
			continue
		elif n <= low or n >= high:
			print('Number is not between high and low values.\n')
			continue

		numbers.append(n)
		print('Result =', end = ' ')
		if n == lucky:
			print('EQUAL')
			searching = False
		else:
			if n > lucky:
				print('HIGH')
				high = n
			else:
				print('LOW')
				low = n
			tryes += 1
			print('Help:', end = ' ')
			print('High =', high, end = ' ')
			print('Low =', low, end = ' ')
			middle = round((high - low) / 2 + low)
			print('Middle =', middle)
			print('Possible numbers count:', high - low - 1, end = '\n\n')
	statistics(numbers, lucky)

def exit():
	print('Goodbye')
	return 'exit'

def main():
	menu_items = ['New Game', 'Settings', 'Instructions', 'Exit']
	menu_funcs = [new_game, settings, instructions, exit]
	program_cycle('Welcome to Magic Number', menu_items, menu_funcs)

if __name__ == '__main__': main()
