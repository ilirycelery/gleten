import os, platform
op_sy = platform.system()

#Function not indexed
def clearConsole():
	if op_sy == "Windows":
		os.system("cls")

	else:
		os.system("clear")


#makefile
def makeFile(dirc, file, text):
	dirc = str(dirc)
	file = str(file)
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

def moveFile(initial_dir, final_dir):
	file_to_move = input("arrastra el archivo a mover aquí: ")
	destiny = input("arrastra aqui la carpeta de destino: ")

def removeFile(file_to_remove):
	if op_sy == "Windows":
		os.system("DEL /F /A "+file_to_remove)

	else:
		os.system("rm "+file_to_remove)

def removeDir(dir_to_remove):
	if op_sy == "Windows":
		os.system("rmdir "+dir_to_remove)

	else:
		os.system("rmdir "+dir_to_remove)
