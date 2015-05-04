# Engine.py

import os

def clear_screen():
	os.system('cls')

def display_program_title(name):
	print('\n' + name)

def display_menu_title(name, n = 20):
	print('\n' + n * '*' + '\n\t' + name + '\n' + n * '*' + '\n')

def display_menu(items, name = 'MENU'):
	display_menu_title(name)
	for n in range(len(items)):
		print('{}: {}'.format(n + 1, items[n]))

def get_input(funcs):
	choice = int(input('> '))
	if choice > len(funcs) or choice < 0:
		print('Invalid input.')
	else:
		funcs[choice - 1]()

def exit():
	global running
	running = False
	print('Goodbye')

running = True

def program_cycle(program_title, menu_items, funcs):
	clear_screen()
	display_program_title(program_title)
	menu_items.append('Exit')
	funcs.append(exit)

	while running:
		display_menu(menu_items)
		get_input(funcs)
