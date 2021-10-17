"""Funciones que van a ser ejecutadas en
main y estan también en el indice (index)"""

import os, platform

#Function not indexed
def clearConsole():
	op_sy = platform.system()
	if op_sy == "Windows":
		os.system("cls")

	else:
		os.system("clear")


#makefile
def makeFile(dirc, file, method, text):
	if (dirc, file, method, text) == None:
		pass
	dirc = str(dirc)
	file = str(file)
	method = str(method)
	text = text or text
	f=open(dirc+"/"+file, "w")
	f.write(text+os.linesep)
	f.close()
	print("File <"+file+"> created, content: " + text)
	input()

#makeDir
def makeDir(dirc):
	dirc = str(dirc)
	os.mkdir(dirc)
	print("Directory <"+dirc+"> created!")

def makeInput():
	pass

def ubication():
	ubication_sys = os.listdir()
	ubication_sys = str(ubication_sys)
	print(ubication_sys)