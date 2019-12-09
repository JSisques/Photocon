from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import *
import os
import shutil

class Option1:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.origin = self.askForOrigin(self.root)
        self.destiny = self.askForDestiny(self.root)
        self.root.destroy()

        if self.destiny != "":
            self.copyFiles()
            self.renameFiles()

    def askForOrigin(self, root):
        self.root.update() #for close the filedialog
        print("Selecciona la carpeta origen")
        origin = filedialog.askdirectory()
        return origin

    def askForDestiny(self, root):
        root.update() #for close the filedialog
        print("Selecciona la carpeta destino")
        destiny = filedialog.askdirectory()
        return destiny

    def copyFiles(self):
        for file in os.listdir(self.origin):
            shutil.copy2(self.origin + os.path.sep + file, self.destiny + os.path.sep + file)

    def renameFiles(self):
        name = input("Escriba el nombre del archivo: ")
        count = 1
        totalFiles = len([name for file in os.listdir(self.destiny) if os.path.isfile(self.destiny + os.path.sep + file)])

        for file in os.listdir(self.destiny):
            if file[0] != "." and os.path.isfile(self.destiny + os.path.sep + file):
                extension = file[-4:]
                if extension[0] != ".": #if extension has more than 3 characters
                    extension = file[-5:]

                os.rename(self.destiny + os.path.sep + file, self.destiny + os.path.sep + name + " "+ str(count) + extension)
                print("[" , count, "/", totalFiles - 1 ,"] Ronombrado ", file ," ==>", name + " "+ str(count) + extension)
                count += 1