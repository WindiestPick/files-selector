from importlib.resources import path
import os
import glob
from readPdf import getCPF


def List_files_in(path):
    os.chdir(path[0])
    files = glob.glob('*.pdf')
    os.chdir(path[2])
    return files

def PesquisaCPFPDF(path, cpf):
    files = List_files_in(path)
    #arq = GetCpfCache(cpf, path[2])
    #if arq == "":
    for i in range(len(files)):
        cpfArq = getCPF(path[1] + files[i])
           
        if (cpf == cpfArq):
            #SetCpfCache(cpf, files[i], path[2])
            return files[i]

