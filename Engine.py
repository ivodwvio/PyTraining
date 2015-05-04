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
	funcs[choice - 1]()

running = True

def program_cycle(program_title, menu_items, funcs):
	clear_screen()
	display_program_title(program_title)

	while running:
		display_menu(menu_items)
		if get_input(funcs) == 'exit':
			break
