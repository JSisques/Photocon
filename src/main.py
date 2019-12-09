from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import *
import os
import shutil

def main():
    while True:
        option = menu()
        if option == 1:
            option1()
        elif option == 0:
            break


def menu():
    print("**************** PHOTOCON ****************")
    print("[1] ==> Organizar archivos")
    print("[2] ==> Covertir fotos (NO IMPLEMENTADO))")
    print("[0] ==> Salir")
    option = int(input("Elige una opcion: "))
    return option


def option1():
    root = Tk()
    root.withdraw()
    root.update() #for close the filedialog
    print("Selecciona la carpeta origen")
    origin = filedialog.askdirectory()
    root.update() #for close the filedialog
    print("Selecciona la carpeta destino")
    destiny = filedialog.askdirectory()

    root.destroy()

    for file in os.listdir(origin):
        shutil.copy2(origin + os.path.sep + file, destiny + os.path.sep + file)

    name = input("Escriba el nombre del archivo: ")
    count = 1
    for file in os.listdir(destiny):
        if file[0] != ".":
            extension = file[-4:]
            if extension[0] != ".":
                extension = file[-5:]

            os.rename( destiny + os.path.sep + file, destiny + os.path.sep + name + " "+ str(count) + extension)
            count += 1


main()