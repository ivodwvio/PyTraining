# MagicNumber.py

import random
import os
from enum import IntEnum

MAX_VALUE = 1000

class Direction(IntEnum):
	Idle = 0
	Upwards = 1
	Downwards = 2

class MenuItems(IntEnum):
	NewGame = 1
	Settings = 2
	Instructions = 3
	Exit = 4

def display_menu_title(name, n = 20):
	print('\n' + n * '*')
	print('\t' + name)
	print(n * '*')
	print()

def display_menu():
	display_menu_title('MENU')
	print('1: New Game')
	print('2: Settings')
	print('3: Instructions')
	print('4: Exit')

def clear_screen():
	os.system('cls')

def instructions():
	display_menu_title('Instructions', 30)
	print('The computer have a number between 0 and MAX_VALUE.')
	print('MAX_VALUE by default is 1000. You can set it in Settings.')
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

def main():
	clear_screen()
	print('\nWelcome to Magic Number')
	running = True
	direction = Direction.Idle

	while running:
		display_menu()
		choice = int(input('> '))

		if choice == MenuItems.NewGame:
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
					direction = Direction.Idle
				else:
					if n > lucky:
						print('HIGH')
						high = n
						direction = Direction.Downwards
					else:
						print('LOW')
						low = n
						direction = Direction.Upwards
					tryes += 1
					print('Help:', end = ' ')
					print('High =', high, end = ' ')
					print('Low =', low, end = ' ')
					middle = round((high - low) / 2 + low)
					print('Middle =', middle)
					print('Possible numbers count:', high - low - 1, end = '\n\n')
			statistics(numbers, lucky)
		elif choice == MenuItems.Settings:
			settings()
		elif choice == MenuItems.Instructions:
			instructions()
		elif choice == MenuItems.Exit:
			running = False

	print('Goodbye.')

if __name__ == '__main__': main()
