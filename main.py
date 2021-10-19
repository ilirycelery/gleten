from functions.functions import *

import sys, os, platform
from time import sleep	
op_sy = platform.system()

#historial
history = []


def main():
	clearConsole()
	for infhistory in history:
		print("~"+infhistory)
	commands = input("start: ")

	if commands == 'makefile':
		history.append(commands)
		input_dirc = input("Directory: ")
		input_file = input("File name: ")

		input_text = input("content: ")
		try:
			makeFile(input_dirc, input_file, input_text)

		except FileNotFoundError:
			print("Directorio de creación de carpeta no encontrado.")
			input()
			return main()

		input()
		return main()

	elif commands == 'makedir':
		history.append(commands)
		input_makedir = input("Nombre del directorio: ")
		makeDir(input_makedir)
		print("Directorio creado")
		input()
		return main()

	elif commands == 'input':
		history.append(commands)
		input_input = input("message: ")
		condition_input = input("enable condition? y/n: ")
		if condition_input == 'y':
			condition_to_enable_input = input("function: ")

		input()
		return main()

	elif commands == 'ubication':
		ubicationreq = os.listdir()
		for infubication in ubicationreq:
			print(infubication)

		input()
		return main()

	elif commands == 'removeFile':
		file = input("Arrastra el archivo a eliminar: ")
		removeFile(file)
		print("Archivo eliminado!")
		input()
		return main()

	elif commands == 'removeDir':
		directory = input("Directorio a eliminar: ")
		removeDir(directory)
		print("Directorio eliminado")
		input()
		return main()

	elif commands == 'exit' or 'Exit':
		exit()

	else:
		history.append(commands)
		print("Command not found")
		sleep(0.2)
		return main()



if __name__ == '__main__':
	main()
