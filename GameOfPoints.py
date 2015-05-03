# GameOfPoints.py

from MagicNumber import clear_screen, display_program_title, display_menu
from enum import IntEnum
import random

class MenuItems(IntEnum):
	Addition = 1
	Subtraction = 2
	Multiplication = 3
	Division = 4
	Mix = 5
	Exit = 6

def addition():
	pass

def subtraction():
	pass

def multiplication():
	pass

def division():
	pass

def mix():
	pass

def main():
	clear_screen()
	display_program_title('Welcome to Game Of Points')
	running = True
	points = 0
	a = b = 0

	while running:
		display_menu(['Addition', 'Subtraction', 'Multiplication', 'Division', 'Mix', 'Exit'])
		choice = int(input('> '))

		print('Points:', points)
		a = random.randint(1, 100)
		b = random.randint(1, 100)
		result = int(input('Task: {} + {} = '.format(a, b)))
		if result == a + b:
			points += 1
		elif result == 0:
			running = False
		print()

if __name__ == '__main__': main()
