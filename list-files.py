import os
import glob
from os import walk


def list_files_in(path, archive):
    for filenames in walk(path):
        archive.extend(filenames)
        break
    return archive


def show(archive):
    for i in range(len(archive)):
        print(archive[i])


def show_archives(archive):
    for i in range(len(archive)):
        print(i, ' - ', archive[i])


def search_files(path, archive):
    os.chdir(path)
    text = input("Nome do arquivo: ")
    archive = glob.glob('*' + text + '*.*')
    return archive


def open_file(path, archive):
    select = int(input("Numero do arquivo que deseja abrir: "))
    os.startfile(path + archive[select])


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
archives = []
search = []
files = list_files_in(local, archives)
show(archives)
search = search_files(local, archives)
show_archives(search)
open_file(local, search)
