from importlib.resources import path
import os
import glob
import io
from readDocx import GetCPf
from tkinter import *
from tkinter.ttk import *


def List_files_in(path):
    os.chdir(path[0])
    files = glob.glob('*.docx')
    lst = glob.glob('*.doc')
    for i in lst:
        files.append(i)
    os.chdir(path[2])
    return files

def PesquisaCPF(path, cpf):
    files = List_files_in(path)
    arq = GetCpfCache(cpf, path[2])
    if arq == "":
        for i in range(len(files)):
            cpfArq = GetCPf(path[1] + files[i])
           
            if (cpfArq.__contains__(cpf.lower())):
                SetCpfCache(cpf, files[i], path[2])
                return files[i]
    else:
        return arq

def SetCpfCache(cpf, nomeArq, path):
    log = io.open(path + "logCpf.txt","a", encoding="utf-8")
    log.write("\n"+cpf + ':' + nomeArq)
    log.close()
    
def GetCpfCache(cpf, path):
    log = io.open(path + "logCpf.txt", "r", encoding="utf-8")
    listaDeCpf = log.readlines()
    for i in range(len(listaDeCpf)):
        cpfArq = listaDeCpf[i].split(":")
        if cpfArq[0] == cpf:
            log.close()
            return cpfArq[1].replace('\n', '')
    log.close()
    return ""

def AtualizaCache(path, ws, pb1):
    files = List_files_in(path)
    log = io.open("logCpf.txt", "w")
    log.write("")
    log.close()

    jump = 100 / len(files)

    for i in range(len(files)):
        ws.update_idletasks()
        pb1['value'] += jump

        cpfArq = GetCPf(path[1] + files[i])
        SetCpfCache(cpfArq, files[i], path[2])

    pb1["value"] = 0
    ws.update_idletasks()




#Show_files(files)