# GameOfPoints.py

from MagicNumber import clear_screen,
	display_program_title, display_menu, exit, get_input
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
	points = 0
	a = b = 0
	print('Points:', points)
	a = random.randint(1, 100)
	b = random.randint(1, 100)
	result = int(input('Task: {} + {} = '.format(a, b)))
	if result == a + b:
		points += 1
	elif result == 0:
		running = False
	print()

def subtraction():
	pass

def multiplication():
	pass

def division():
	pass

def mix():
	pass

running = True

def main():
	clear_screen()
	display_program_title('Welcome to Game Of Points')	

	while running:
		display_menu(['Addition', 'Subtraction', 'Multiplication', 'Division', 'Mix', 'Exit'])
		get_input([addition, subtraction, multiplication, division, mix, exit])

if __name__ == '__main__': main()
