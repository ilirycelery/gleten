from functions.functions import *

"""Archivo principal para que se ejecuten
todas las funciones de Gleten

os: creación y modificación en archivos
sys: parametros de ejecución"""

import sys, os, platform

"""Variables para interpretación e identificacións
(no privadas)"""
op_sy = platform.system()

#historial
history = []


def main():
	clearConsole()
	commands = input("start: ")

	if commands == 'index':
		print(COMMANDS["index"])
		history.append(commands)
		return main()

	elif commands == 'project':
		name_program = input("Nombre del proyecto: ")
		aut_program = input("Nombre del creador: ")


	elif commands == 'makefile':
		history.append(commands)
		input_dirc = input("Directory: ")
		input_file = input("File name: ")
		input_method = input("read or write? r/w: ")
		input_text = input("content: ")
		makeFile(input_dirc, input_file, input_method, input_text)
		return main()

	elif commands == 'makedir':
		input_makedir = input("Nombre del directorio: ")
		makeDir(input_makedir)
		history.append(commands)
		return main()

	elif commands == 'input':
		input_input = input("message: ")
		condition_input = input("enable condition? y/n: ")
		if condition_input == 'y':
			condition_to_enable_input = input("function: ")
		history.append(commands)

	elif commands == 'ubication':
		ubicationreq = os.listdir()
		ubicationreq = str(ubicationreq)
		print(ubicationreq)

	else:
		print("Command not found")
		history.append(commands)
		sleep(0.2)
		clearConsole()
		return main()



if __name__ == '__main__':
	main()