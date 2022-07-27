from doctest import master
from tkinter import *
from tkinter.ttk import *
import os
from turtle import title
from pesquisaCPF import *
from pesquisaVulgo import update_cache
import time


class Configuracao():
    def __init__(self, master=None):
        self.path = []
        self.fontePadrao = ("Arial", "10")
        self.fonteAtualiza = ("Arial", "8")
        self.fonteGrande = ("Arial Negrito", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer.pack(pady = 10)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.pack(pady = 10)

        self.quartoContainer = Frame(master)
        self.quartoContainer.pack(pady = 10)

        self.barContainer = Frame(master)
        self.barContainer.pack(pady = 10)

        self.qintoContainer = Frame(master)
        self.qintoContainer.pack(pady = 10)

        self.path1Label = Label(self.segundoContainer, 
                    text="Adicionar um diretório padrão", font=self.fontePadrao)
        self.path1Label.pack()

        self.path1 = Entry(self.segundoContainer)
        self.path1["font"] = self.fontePadrao
        self.path1["width"] = 34
        self.path1.pack(side=LEFT)

        self.configuracao = Button(self.segundoContainer, text="Adicionar")
        self.configuracao.pack(side="right")
        self.configuracao["command"] = self.setPath
        
        self.pathP = Label(self.terceiroContainer, text=self.fontePadrao)
        self.pathP.pack()

        self.atualizar = Label(self.quartoContainer, justify="left", text="Atualizar a cache pode levar alguns\nsegundos, essa função é necessária\npara tornar a pesquisa mais ágil", font=self.fonteAtualiza)
        self.atualizar.pack(side="left")

        self.configuracao = Button(self.quartoContainer, text="Atualizar Cache")
        self.configuracao.pack(side="right")
        self.configuracao["command"] = self.start

        self.status = Label(self.barContainer, font=self.fonteGrande)
        self.status['text'] = ''
        self.status.pack()

        self.pb1 = Progressbar(self.barContainer, orient=HORIZONTAL, length=300, mode='determinate',)
        self.pb1.pack(expand=True, side=BOTTOM)

        self.sair = Button(self.qintoContainer, text="Sair")
        self.sair.pack(side="right")
        self.sair["command"] = master.destroy

        self.getPath()

    def setPath(self):
        msg = Toplevel(master)
        msg.title("Mensagem")
        msg.iconbitmap(".\\photo\\Finding.ico")
        msg.geometry("300x150")

        mensagem = Label(msg, font=self.fontePadrao, text="Deseja atualizar o diretório?")
        mensagem.pack(pady=20)

        sim = Button(msg, text="Sim")
        sim.pack(side="right", padx=20)
        sim["command"] = self.atualizarPath

        nao = Button(msg, text="Não")
        nao.pack(side="left", padx=20)
        nao["command"] = msg.destroy

        msg.mainloop()
        
    def getPath(self):
        arq = open("config.txt","r")
        text = arq.readlines()
        self.path = []
        for i in text:
            self.path.append(i.replace("\n", ""))
        self.pathP["text"] = "Diretório atual: "+self.path[0]
        arq.close()

    def start(self):
        self.status["text"] = "Progresso: 0/2"
        self.status.pack()
        AtualizaCache(self.path, self.barContainer, self.pb1)
        self.status["text"] = "Progresso: 1/2"
        self.barContainer.update_idletasks()
        update_cache(self.path, self.barContainer, self.pb1)
        self.status["text"] = "Progresso: 2/2"
        self.barContainer.update_idletasks()
        self.pb1["value"] = 0
        time.sleep(2)
        self.status['text'] = ''

    def atualizarPath(self):
        arq = open("config.txt","w")
        text = self.path1.get()
        CURR_DIR = os.getcwd()
        lst = [text+"\n", text+"\\\n",CURR_DIR+"\\"]
        arq.writelines(lst)
        self.path1.delete(0,END)
        arq.close()
        self.getPath()