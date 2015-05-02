# MagicNumber.py

import random
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

def display_menu():
	display_menu_title('MENU')
	print('1: New Game')
	print('2: Settings')
	print('3: Instructions')
	print('4: Exit')

def instructions():
	display_menu('Instructions', 30)
	print('The computer have a number between 1 and MAX_VALUE.')
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
	display_menu('Settings')
	answer = input('Do you want to change the MAX_VALUE?(y/n):')
	if answer == 'y':
		MAX_VALUE = int(input('new value = '))
	elif answer == 'n':
		return
	else:
		print('Invalid ansewr.')

def main():
	print('\nWelcome to Magic Number')
	running = True
	direction = Direction.Idle

	while running:
		display_menu()
		choice = int(input('> '))

		if choice == MenuItems.NewGame:
			lucky = random.randint(1, MAX_VALUE)
			
			print('\nGame Start\n')
			print('Help: start with MAX_VALUE / 2 =', round(MAX_VALUE / 2))
			searching = True
			tryes = 0
			high = MAX_VALUE
			low = 1
			tryes = 0
			numbers = []

			while searching:
				n = int(input('Guess {}: '.format(tryes + 1)))
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
					print('\nHelp:')
					print('High =', high)
					print('Low =', low)
					middle = round((high - low) / 2 + low)
					print('Middle =', middle)
					print()
			statistics(numbers, lucky)
		elif choice == MenuItems.Settings:
			settings()
		elif choice == MenuItems.Instructions:
			instructions()
		elif choice == MenuItems.Exit:
			running = False

	print('Goodbye.')

if __name__ == '__main__': main()
