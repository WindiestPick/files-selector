from cProfile import label
from cgitb import reset, text
from numbers import Number
from pdb import Restart
from turtle import resetscreen
from pesquisaNome import PesquisaNome
from pesquisaCPF import PesquisaCPF
from tkinter import *
import os

class Application():
    arquivo = []

    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.nomeContainer = Frame(master)
        self.nomeContainer["padx"] = 20
        self.nomeContainer.pack()

        self.cpfContainer = Frame(master)
        self.cpfContainer["padx"] = 20
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
        self.cpfLabel.pack(side=BOTTOM)
        self.cpfLabel.pack(side=LEFT)

        self.cpfArq = Entry(self.cpfContainer)
        self.cpfArq["width"] = 30
        self.cpfArq["font"] = self.fontePadrao
        self.cpfArq.pack(side=BOTTOM)
        self.cpfArq.pack(side=LEFT)

        self.buscarCpf = Button(self.cpfContainer)
        self.buscarCpf["text"] = "Buscar por CPF"
        self.buscarCpf.pack(side=BOTTOM)
        self.buscarCpf.pack(side=LEFT)
        self.buscarCpf["command"] = self.PesquisaC


        self.listArq = Label(self.terceiroContainer, font=self.fontePadrao)
        self.listArq.pack(side=LEFT)

        
        self.numeroArq = Entry(self.quartoContainer)
        self.numeroArq["width"] = 10
        self.numeroArq["font"] = self.fontePadrao
        self.numeroArq.pack(side=LEFT)
        
        self.abrir = Button(self.quartoContainer)
        self.abrir["text"] = "abrir"
        self.abrir.pack(side=RIGHT)
        self.abrir["command"] = self.AbreArq

        self.limpa = Button(self.cleanerContainer)
        self.limpa["text"] = "limpar"
        self.limpa.pack()
        self.limpa["command"] = self.clean


    def PesquisaN(self):
        pesquisa = self.nomeArq.get()
        lista = PesquisaNome(pesquisa, path[0])
        self.arquivo = lista
        nomes = ''
        if (len(lista) > 0):
            for i in range(len(lista)):
                nomes += "\n" + str(i+1) + " - " + lista[i]
            self.listArq["text"] = nomes
        else:
            self.listArq["text"] = "Nenhum resultado encontrado"
    
    def PesquisaC(self):
        pesquisa = self.cpfArq.get()
        formato = ''
        for i in range(len(pesquisa)):
            if (pesquisa[i] != ' ' and pesquisa[i] != '-' and pesquisa[i] != '.'):
                formato += pesquisa[i]
        if pesquisa != "":
            nome = PesquisaCPF(path, formato)
            if (nome != None):
                self.arquivo = [nome]
                self.listArq["text"] = "1 - " + nome
            else:
                self.listArq["text"] = "Nenhum arquivo encontrado"
        else:
            self.listArq["text"] = "Pesquisa por CPF não aceita campo vazio"


    def AbreArq(self):
        numero = self.numeroArq.get()
        if numero != "":
            os.startfile(path[1] + self.arquivo[int(numero) - 1])
    
    def clean(self):
        self.listArq['text'] = ''
        self.numeroArq.delete(0,END)
        self.nomeArq.delete(0,END)
        self.cpfArq.delete(0,END)
        


    


path = ["C:\\Users\\Marketing\\Documents\\Teste","C:\\Users\\Marketing\\Documents\\Teste\\"]
root = Tk(className="Finding 2")
Application(root)
root.mainloop()



'''
path = ["C:\\Users\\Marketing\\Documents\\Teste","C:\\Users\\Marketing\\Documents\\Teste\\"]

pesquisa = input("digite o nome da pessoa: ")

lista = PesquisaNome(pesquisa, path[0])
for i in range(len(lista)):
    print( i+1 ," - ", lista[i])

pesquisa = input("digite o cpf que deseja pesquisar: ")

print(PesquisaCPF(path,pesquisa))
'''

