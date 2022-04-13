import os
import glob

def list_files_in(path,files):
    
    for (dirpath, dirnames, filenames) in os.walk(path):
      files.extend(filenames)
      break
    
def show_files(files):
    
    for numero,arquivo in enumerate(files):
        print(arquivo)

def menu():

    print("---------------- MENU ----------------")
    print("1 - Mostrar fotos comida")
    print("5 - Sair")
    print("--------------------------------------\n")


def choose_your_destiny():
    
    while(True):
        destiny = int(input("Qual opção deseja(1 ou 5):"))
        if(destiny == 1):
            path = "G:\Imagens de Produtos\comida\\"
            current_directory = os.path.dirname(os.path.abspath(path))
            os.chdir('G:\Imagens de Produtos\comida')
            text = input("Nome do arquivo: ")
            files = glob.glob( '*'+ text +'*.png')
            print("\n\n-------- Arquivos Encontrados --------")
            for i in range(len(files)):
                print(i , ' - ' , files[i])
            print("--------------------------------------\n\n")
            selecao = int(input("Numero do arquivo que deseja abrir: "))
            os.startfile(path + files[selecao])

            continue;
            
        elif(destiny == 5):
            break       

menu()
choose_your_destiny()

