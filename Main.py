from cgitb import text
from logging import PlaceHolder
from tkinter import *
from Config import Configuration
import os

class Application():
    arquivo = []
    path = []

    def __init__(self, master=None):

        self.getPath()

        #Fonts

        self.defaultFont = ("Arial", "15")
        self.mensageFont = ("Arial", "11")
        self.showFileFont = ("Arial", "11")
        
        #Containers

        self.window = Frame(master)
        self.window["pady"] = 10
        self.window.pack()

        self.searchConteiner = Frame(master)
        self.searchConteiner["padx"] = 20
        self.searchConteiner["pady"] = 5
        self.searchConteiner.pack()

        self.fileConteiner = Frame(master)
        self.fileConteiner["padx"] = 20
        self.fileConteiner.pack()

        self.toolConteiner = Frame(master)
        self.toolConteiner["pady"] = 20
        self.toolConteiner.pack()


        #Labels

        self.windoWelcome = Label(self.window, text="Bem vindo ao Finding", font=self.defaultFont)
        self.windoWelcome.pack()

        self.windowSeach = Label(self.window, text="\nPesquisa de arquivos", font=self.defaultFont)
        self.windowSeach.pack()

        self.windowMensage = Label(self.window, text="(Pesquisas disponíveis: vulgo, cpf e nome)", font=self.mensageFont)
        self.windowMensage.pack()

        self.fileLabel = Label(self.fileConteiner,text="Arquivos encontrados", font= self.showFileFont)
        self.fileLabel.pack(side=TOP)
        

        #Entry

        self.searchEntry = Entry(self.searchConteiner)
        self.searchEntry["width"] = 30
        self.searchEntry["font"] = self.defaultFont
        self.searchEntry.pack(side=TOP)
        self.searchEntry.pack(side=LEFT)

        #Button
        
        self.searchButton = Button(self.searchConteiner)
        self.searchButton["text"] =  "Pesquisar"
        self.searchButton.pack(expand=1)
        self.searchButton.pack(side=LEFT)

        self.cleanButton = Button(self.toolConteiner)
        self.cleanButton["text"] = "Limpar"
        self.cleanButton.pack(expand=1)
        self.cleanButton.pack(side=LEFT)

        self.configButoon = Button(self.toolConteiner)
        self.configButoon["text"] = "Configurações"
        self.configButoon.pack(expand=1)
        self.configButoon.pack(side=LEFT)
        self.configButoon["command"] = self.startConfig


        #Scrollbar

        self.fileScroll = Scrollbar(self.fileConteiner)
        self.fileScroll.pack(side="right", fill=BOTH)

        #ListBox

        self.fileListBox = Listbox(self.fileConteiner, yscrollcommand=self.fileScroll.set)
        self.fileListBox["width"] = 50
        self.fileListBox.pack(side="bottom", fill="both")


        #Scrollbar ListBox config

        self.fileScroll.config(command=self.fileListBox.yview)

        self.getPath()

    def getPath(self):
        if (self.path != []):
            arq = open(self.path[2] + "config.txt", "r")
        else:
            arq = open("config.txt", "r")
        text = arq.readline()
        save = []
        for i in text:
            save.append(i.replace("\n",""))
        arq.close()
        return save


    def startConfig(self):
        configuration = Tk(className="Fiding>>>Configuration")
        Configuration(configuration)
        configuration.mainloop()


root = Tk(className = "Finding")
Application(root)
root.mainloop()
