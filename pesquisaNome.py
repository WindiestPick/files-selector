import os
import glob


#def choose_your_destiny():
#    
#    while(True):
#        destiny = int(input("Qual opção deseja(1 ou 5):"))
#       if(destiny == 1):
#            path = "C:\Users\Marketing\Documents\Teste\\"
#            current_directory = os.path.dirname(os.path.abspath(path))
#            os.chdir('C:\Users\Marketing\Documents\Teste')
#            text = input("Nome do arquivo: ")
#            files = glob.glob( '*'+ text +'*.png')
#            print("\n\n-------- Arquivos Encontrados --------")
#            for i in range(len(files)):
#                print(i , ' - ' , files[i])
#            print("--------------------------------------\n\n")
#            selecao = int(input("Numero do arquivo que deseja abrir: "))
#            os.startfile(path + files[selecao])
#
#            continue;
#            
#        elif(destiny == 5):
#            break       


def PesquisaNome(text,path):
    os.chdir(path)
    files = glob.glob( '*'+ text +'*.*')
    return files
