from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import *
import os
import shutil
from option1 import Option1

def main():
    while True:
        option = menu()
        if option == 1:
            option1 = Option1()
        elif option == 0:
            sys.exit(1)


def menu():
    print("**************** PHOTOCON ****************")
    print("[1] ==> Organizar archivos")
    print("[2] ==> Covertir fotos (NO IMPLEMENTADO))")
    print("[0] ==> Salir")
    option = int(input("Elige una opcion: "))
    return option

main()