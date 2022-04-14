import os
import glob
from readDocx import GetCPf


def List_files_in(path):
    current_directory = os.path.dirname(os.path.abspath(path))
    os.chdir(path)
    files = glob.glob('*.docx')
    return files

def PesquisaCPF(path, cpf):
    files = List_files_in(path[0])
    for i in range(len(files)):
        cpfArq = GetCPf(path[1] + files[i])
        if (cpf == cpfArq):
            return files[i]



#Show_files(files)