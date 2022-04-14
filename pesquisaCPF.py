import os
from docx import Document
from docx.shared import Inches

def List_files_in(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
      files.extend(filenames)
    return files
    
def Show_files(files):
    
    for numero,arquivo in enumerate(files):
        print(arquivo)

def PesquisaCPF(path):
    files = List_files_in(path[0])
    for i in range(len(files)):
        document = Document(docx = path[1] + files[i])
        
        
        

path = ["D:\\","D:\\"]

PesquisaCPF(path)


#Show_files(files)