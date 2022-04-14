import os
import glob
from os import walk

def list_files_in(path,files):
    
    for (dirpath, dirnames, filenames) in walk(path):
      files.extend(filenames)
      break
    return files
    
def show(files):

    for i in range(len(files)):
        print(files[i])
    
        
def showEnumarete(files):
    
    for i in range(len(files)):
        print(i , ' - ' , files[i])


def search_files(path,filesToSearch):
    os.chdir(path)
    text = input("Nome do arquivo: ")
    filesToSearch = glob.glob( '*'+ text +'*.*')
    return filesToSearch

def open_file(path,files):

    selecao = int(input("Numero do arquivo que deseja abrir: "))
    os.startfile(path + files[selecao])

'''
def choose_your_destiny():
    
    while(True):
        destiny = int(input("Qual opção deseja(1 ou 5):"))
        if(destiny == 1):
            path = "G:\Imagens de Produtos\comida\\"
            current_directory = os.path.dirname(os.path.abspath(path))
            os.chdir('G:\Imagens de Produtos\comida')
            text = input("Nome do arquivo: ")
            files = glob.glob( '*'+ text +'*.png')
            print("\n-------- Arquivos Encontrados --------")
            for i in range(len(files)):
                print(i , ' - ' , files[i])
            print("--------------------------------------\n\n")
            selecao = int(input("Numero do arquivo que deseja abrir: "))
            os.startfile(path + files[selecao])

            continue;
            
        elif(destiny == 5):
            break       
'''

local = "D:\\"
files = []
search = []
files = list_files_in(local,files)
show(files)
search = search_files(local,files)
showEnumarete(search)
open_file(local,search)

