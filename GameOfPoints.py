# GameOfPoints.py

import random
from Engine import program_cycle
from Engine import display_menu_title

points = 0

def addition():
	display_menu_title('Addition', 25)
	print('Answer with 0 if you want to stop.')
	running = True
	global points
	while running:
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

def statistics():
	global points
	display_menu_title('Statistics', 30)
	print('Points:', points)

def main():
	menu_items = ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Mix', 'Statistics']
	menu_funcs = [addition, subtraction, multiplication, division, mix, statistics]
	program_cycle('Welcome to Game Of Points', menu_items, menu_funcs)

if __name__ == '__main__': main()
