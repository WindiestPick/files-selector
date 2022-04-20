from pesquisaNome import PesquisaNome
from pesquisaCPF import PesquisaCPF
from config import Configuracao
from tkinter import *
import os

class Application():
    arquivo = []
    path = []

    def __init__(self, master=None):
        self.getPath()
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.nomeContainer = Frame(master)
        self.nomeContainer["padx"] = 20
        self.nomeContainer["pady"] = 5
        self.nomeContainer.pack()

        self.cpfContainer = Frame(master)
        self.cpfContainer["padx"] = 20
        self.cpfContainer["pady"] = 5
        self.cpfContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
        
        self.cleanerContainer = Frame(master)
        self.cleanerContainer["pady"] = 20
        self.cleanerContainer.pack()


        self.scrollbar = Scrollbar(self.terceiroContainer)
        self.scrollbar.pack(side="right", fill=BOTH)
        
        self.nomeLabel = Label(self.primeiroContainer, text='Busca Documentos', font=self.fontePadrao)
        self.nomeLabel.pack()

        self.nomeLabel = Label(self.nomeContainer,text="Nome do Arquivo", font=self.fontePadrao)
        self.nomeLabel.pack(side=TOP)
        self.nomeLabel.pack(side=LEFT)

        self.nomeArq = Entry(self.nomeContainer)
        self.nomeArq["width"] = 30
        self.nomeArq["font"] = self.fontePadrao
        self.nomeArq.pack(side=TOP)
        self.nomeArq.pack(side=LEFT)

        self.buscar = Button(self.nomeContainer)
        self.buscar["text"] = "Buscar por nome"
        self.buscar.pack(expand=1)
        self.buscar.pack(side=LEFT)
        self.buscar["command"] = self.PesquisaN
        
        
        self.cpfLabel = Label(self.cpfContainer,text="Numero do CPF", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)

        self.cpfArq = Entry(self.cpfContainer)
        self.cpfArq["width"] = 30
        self.cpfArq["font"] = self.fontePadrao
        self.cpfArq.pack(side=LEFT)

        self.buscarCpf = Button(self.cpfContainer)
        self.buscarCpf["text"] = "Buscar por CPF"
        self.buscarCpf.pack(side=LEFT)
        self.buscarCpf["command"] = self.PesquisaC


        self.cpfLabel = Label(self.terceiroContainer,text="Selecione um Arquivo: ", font=self.fontePadrao)
        self.cpfLabel.pack(side="top")

        self.listbox = Listbox(self.terceiroContainer, yscrollcommand=self.scrollbar.set)
        self.listbox["width"] = 50
        self.listbox.pack(side="bottom", fill="both")

        self.scrollbar.config(command=self.listbox.yview)
        
        self.abrir = Button(self.quartoContainer)
        self.abrir["text"] = "abrir"
        self.abrir["width"] = 30
        self.abrir["height"] = 2
        self.abrir.pack(side=RIGHT)
        self.abrir["command"] = self.AbreArq

        self.limpa = Button(self.cleanerContainer)
        self.limpa["text"] = "limpar"
        self.limpa.pack(side="left")
        self.limpa["width"] = 20
        self.limpa["command"] = self.clean
        
        self.configuracao = Button(self.cleanerContainer, text="Configurações")
        self.configuracao.pack(side="right")
        self.configuracao["command"] = self.configura

    def PesquisaN(self):
        self.path = self.getPath()
        pesquisa = self.nomeArq.get()
        lista = PesquisaNome(pesquisa, self.path)
        self.arquivo = lista
        nomes = ''
        if (len(lista) > 0):
            self.listbox.delete(0, END)
            for i in range(len(lista)):
                self.listbox.insert("end", "\n" + str(i+1) + " - " + lista[i])
        else:
            self.listbox.delete(0, END)
            self.listbox.insert("end","Nenhum resultado encontrado")
    
    def PesquisaC(self):
        self.path = self.getPath()
        pesquisa = self.cpfArq.get()
        formato = ''
        for i in range(len(pesquisa)):
            if (pesquisa[i] != ' ' and pesquisa[i] != '-' and pesquisa[i] != '.'):
                formato += pesquisa[i]
        if pesquisa != "":
            nome = PesquisaCPF(self.path, formato)
            if (nome != None):
                self.arquivo = [nome]
                self.listbox.delete(0, END)
                self.listbox.insert("end", "\n1" + " - " + nome)
            else:
                self.listbox.delete(0, END)
                self.listbox.insert("end","Nenhum resultado encontrado")
        else:
            self.listbox.delete(0, END)
            self.listbox.insert("end","Pesquisa por CPF não aceita campo vazio")


    def AbreArq(self):
        numero = self.select_item()
        if numero != None:
            if int(numero) <= len(self.arquivo):
                os.startfile(self.path[1] + self.arquivo[int(numero) - 1])
        else:
            os.startfile(self.path[1] + self.arquivo[0])
    
    def clean(self):
        self.listbox.delete(0,END)
        self.nomeArq.delete(0,END)
        self.cpfArq.delete(0,END)
        
    def select_item(self):
        for i in self.listbox.curselection():
            num = self.listbox.get(i).replace('\n', '')
            num = self.listbox.get(i).split(" ")
            return(num[0])
    
    def configura(self):
        conf = Tk(className="Configuração")
        Configuracao(conf)
        conf.mainloop()

    def getPath(self):
            if self.path != []:
                arq = open(self.path[2]+"config.txt","r")
            else:
                arq = open("config.txt","r")
            text = arq.readlines()
            b = []
            for i in text:
                b.append(i.replace("\n",""))
            arq.close()
            return b
    


root = Tk(className="Finding 2")
Application(root)
root.mainloop()


