from email.policy import default
from tkinter import *
import os
from SaveSearch import *

class Configuration():

    def __init__(self, master=None):
        self.path = []
        
        #Fonts

        self.defaultFont = ("Arial", "15")
        self.mensageFont = ("Arial", "11")
        self.showFileFont = ("Arial", "9")
        
        #Containers
        
        self.window = Frame(master)
        self.window["pady"] = 40
        self.window["padx"] = 20
        self.window.pack()

        self.pathConteiner = Frame(master)
        self.pathConteiner["padx"] = 20
        self.pathConteiner["pady"] = 5
        self.pathConteiner.pack()
        
        self.infoConteiner = Frame(master)
        self.infoConteiner["padx"] = 20
        self.infoConteiner["pady"] = 5
        self.infoConteiner.pack()

        self.cacheConteiner = Frame(master)
        self.cacheConteiner["padx"] = 20
        self.cacheConteiner["pady"] = 5
        self.cacheConteiner.pack()

        #Label

        self.windowLabel = Label(self.window, text="Configurações", font=self.defaultFont)
        self.windowLabel.pack()

        self.pathLabel =  Label(self.pathConteiner, text="Adicione o diretório padrão", font=self.defaultFont)
        self.pathLabel.pack()

        self.actualDirectoryLabel = Label(self.infoConteiner, text=self.mensageFont)
        self.actualDirectoryLabel.pack()

        self.updateCacheLabel = Label(self.cacheConteiner, justify="left" ,text="Atualizar a cache pode levar alguns\nsegundos, essa função é necessária\npara tornar a pesquisa mais ágil", font=self.showFileFont) 
        self.updateCacheLabel.pack(side=LEFT)
        

        #Entry

        self.pathEntry = Entry(self.pathConteiner)
        self.pathEntry["width"] = 30
        self.pathEntry["font"] = self.mensageFont
        self.pathEntry.pack(side=LEFT)

        #Button

        self.addPathButton =  Button(self.pathConteiner, text="Adicionar")
        self.addPathButton.pack()
        self.addPathButton["command"] = self.setPath

        self.updateCacheButton = Button(self.cacheConteiner, text="Atualizar Cache", font=self.showFileFont)
        self.updateCacheButton.pack(side=RIGHT)
        self.updateCacheButton["command"] = self.start
        
        self.getPath()

    def setPath(self):
        arq = open("config.txt", "w")
        text = self.pathEntry.get()
        CURR_DIR = os.getcwd()
        directorySaved = [text+"\n", text + "\\\n", CURR_DIR + "\\" ]
        arq.writelines(directorySaved)
        self.pathEntry.delete(0,END)
        arq.close()
        self.getPath()

    def getPath(self):
        arq = open("config.txt", "r")
        putedLines = arq.readlines()
        self.path = []
        for i in putedLines:
            self.path.append(i.replace("\n",""))
        self.actualDirectoryLabel["text"] = "Diretorio atual: " + self.path[0]
        arq.close()

    def start(self):
        update_cache(self.path)
        return