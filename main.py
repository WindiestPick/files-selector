from tkinter.ttk import Style
from pesquisaNome import PesquisaNome
from pesquisaCPF import PesquisaCPF
from pesquisaVulgo import search_vulgo
from pesquisaCpfPdf import PesquisaCPFPDF
from config import Configuracao
from tkinter import *
from tkinter.ttk import *
import os
import win32gui
import win32con

class Application():
    arquivo = []
    path = []

    def __init__(self, master=None):
        self.getPath()

        self.menubar = Menu(master)
        self.file = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label ='Opções', menu = self.file)
        self.file.add_command(label ='Configurações', command = self.configura)
        self.file.add_separator()
        self.file.add_command(label ='Sair', command = master.destroy)

        self.fontePadrao = ("Arial", "10")
        self.fontGrande = ("Arial Black", "15")
        self.fonteSelect = ("Arial negrito", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack(pady = 10)

        self.selectContainer = Frame(master)
        self.selectContainer.pack(pady = 10)

        self.nomeContainer = Frame(master)
        self.nomeContainer.pack(pady = 10)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.pack(pady = 10)

        self.quartoContainer = Frame(master)
        self.quartoContainer.pack(pady = 10)

        self.cleanerContainer = Frame(master)
        self.cleanerContainer.pack(pady = 10)

        self.scrollbar = Scrollbar(self.terceiroContainer)
        self.scrollbar.pack(side="right", fill=BOTH)

        self.scrollbar2 = Scrollbar(self.terceiroContainer, orient="horizontal")
        self.scrollbar2.pack(side=BOTTOM, fill=X)

        self.nomeLabel = Label(self.primeiroContainer, text='Busca Documentos', font=self.fontGrande)
        self.nomeLabel.pack()

        self.radioValue = IntVar()
        self.tiulo = Label(self.selectContainer, text = 'Todos os Arquivos: ', font=self.fonteSelect)
        self.tiulo2 = Label(self.selectContainer, text = 'Arquivos em Docx: ', font=self.fonteSelect)
        self.tiulo3 = Label(self.selectContainer, text = 'Arquivos em PDF: ', font=self.fonteSelect)

        self.rdioOne = Radiobutton(self.selectContainer, text='Nome',
                             variable= self.radioValue, value=0,)

        self.rdioTwo = Radiobutton(self.selectContainer, text='CPF',
                             variable= self.radioValue, value=1) 
        self.rdioThree = Radiobutton(self.selectContainer, text='"Vulgo"',
                             variable= self.radioValue, value=2)
        self.rdioFour = Radiobutton(self.selectContainer, text='CPF 🄱🄴🅃🄰',
                             variable= self.radioValue, value=3)


        self.tiulo.grid(column=1,row=0, sticky="W",padx = 5)
        self.rdioOne.grid(column=2, row=0, sticky="W", padx = 5)
        self.rdioOne["width"]=10

        self.tiulo2.grid(column=1,row=1, sticky="W", padx = 5)
        self.rdioTwo.grid(column=2, row=1, sticky="W", padx = 5)
        self.rdioTwo["width"]=10
        self.rdioThree.grid(column=3, row=1, sticky="W", padx = 5)
        self.rdioThree["width"]=10

        self.tiulo3.grid(column=1,row=2,sticky="W", padx = 5)
        self.rdioFour.grid(column=2, row=2, sticky="W", padx = 5)
        self.rdioFour["width"]=10

        self.pesquisa = Entry(self.nomeContainer)
        self.pesquisa["width"] = 34
        self.pesquisa["font"] = self.fontePadrao
        self.pesquisa.pack(side=TOP)
        self.pesquisa.pack(side=LEFT)

        self.buscar = Button(self.nomeContainer)
        self.buscar["text"] = "Buscar"
        self.buscar["width"] = 10
        self.buscar.pack(expand=1)
        self.buscar.pack(side=LEFT)
        self.buscar["command"] = self.SelecionaPesquisa

        self.cpfLabel = Label(self.terceiroContainer,text="Selecione um Arquivo: ", font=self.fonteSelect)
        self.cpfLabel.pack(side="top")

        self.listbox = Listbox(self.terceiroContainer, yscrollcommand=self.scrollbar.set, 
                                xscrollcommand=self.scrollbar2.set)
        self.listbox["width"] = 50
        self.listbox.pack(side="bottom", fill="both")

        self.listbox.bind('<Double-1>', self.AbreArq)

        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar2.config(command=self.listbox.xview)

        self.limpa = Button(self.cleanerContainer)
        self.limpa["text"] = "limpar"
        self.limpa.pack(side="left")
        self.limpa["width"] = 20
        self.limpa["command"] = self.clean

        master.config(menu = self.menubar)

    def SelecionaPesquisa(self):
        b = self.radioValue.get()
        if b == 0:
            self.PesquisaN()
        elif b == 1:
            self.PesquisaC()
        elif b == 2:
            self.SearchV()
        elif b == 3:
            self.PesquisaCPFPDF()

    def PesquisaN(self):
        self.path = self.getPath()
        pesquisa = self.pesquisa.get()
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
        pesquisa = self.pesquisa.get()
        formato = ''
        t = self.validaCPF(pesquisa)

        if t == 0:
            self.listbox.delete(0, END)
            self.listbox.insert("end","Pesquisa por CPF não aceita letras")
            return

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

    def SearchV(self):
        self.path = self.getPath()
        pesquisa = self.pesquisa.get()

        if pesquisa != "":
            nome = search_vulgo(self.path, pesquisa)
            if (nome != []):
                self.arquivo = nome
                self.listbox.delete(0, END)
                for i in range(len(nome)):
                    self.listbox.insert("end", "\n" + str(i+1) + " - " + nome[i])
            else:
                self.listbox.delete(0, END)
                self.listbox.insert("end","Nenhum resultado encontrado")
        else:
            self.listbox.delete(0, END)
            self.listbox.insert("end","Pesquisa por VULGO não aceita campo vazio")

    def PesquisaCPFPDF(self):
        self.path = self.getPath()
        pesquisa = self.pesquisa.get()
        t = self.validaCPF(pesquisa)
        formato = ''

        if t == 0:
            self.listbox.delete(0, END)
            self.listbox.insert("end","Pesquisa por CPF não aceita letras")
            return

        for i in range(len(pesquisa)):
            if (pesquisa[i] != ' ' and pesquisa[i] != '-' and pesquisa[i] != '.'):
                formato += pesquisa[i]
        if pesquisa != "":
            nome = PesquisaCPFPDF(self.path, formato)
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

    def AbreArq(self, event):
        numero = self.select_item()
        if numero != None:
            if int(numero) <= len(self.arquivo):
                os.startfile(self.path[1] + self.arquivo[int(numero) - 1])
        else:
            os.startfile(self.path[1] + self.arquivo[0])

    def clean(self):
        self.listbox.delete(0,END)
        self.pesquisa.delete(0,END)

    def select_item(self):
        for i in self.listbox.curselection():
            num = self.listbox.get(i).replace('\n', '')
            num = self.listbox.get(i).split(" ")
            return(num[0])

    def configura(self):
        conf = Tk(className="Configuração")
        conf.geometry("400x250")
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

    def validaCPF(self, a):
        alfa = ['1','2','3','4','5','6','7','8','9','-','.']
        for i in a:
            f = 0
            for j in alfa:
                if i == j:
                    f += 1
            if f == 0:
                return 0
        return 1

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)

root = Tk(className="Finding 2")
root.geometry("400x500")
Application(root)
root.mainloop()


