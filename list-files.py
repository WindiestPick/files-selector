import os
import glob
from os import walk

def list_files_in(path,files):
    
    for (dirpath, dirnames, filenames) in walk(path):
      files.extend(filenames)
      break
    
def show_files(files):

    cont = 0
    for numero,arquivo in enumerate(files):
        print(f"",cont,arquivo)
        cont= cont+1

def search_files(path,filesToSearch):
    os.chdir(path)
    text = input("Nome do arquivo: ")
    filesToSearch = glob.glob( '*'+ text +'*.*')
    for i in range(len(filesToSearch)):
        print(i , ' - ' , filesToSearch[i])

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

local = ""
files = []
search = []
list_files_in(local,files)
show_files(files)
search_files(local,search)
open_file(local,files)

