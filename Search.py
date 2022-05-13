import os
import glob
from ReadDocx import *

def name_search(text,path):
    os.chdir(path[0])
    files = glob.glob( '*'+ text +'*.*')
    os.chdir(path[2])
    return files

def in_doc_search(file,fileList):
    #Use docx2txt
    file = file_to_text(file)
    fileList = save_file_text(fileList,file)
    for i in range(len(text)):
        if(text[i] != ""):
            savedlist.append(text[i])
    for i in range(len(savedlist)):
        test = savedlist[i]
        test = test.split(":")
        if(test[0] == "CPF"):
            cpf = ''
            for i in range(len(test[1])):
                if test[1][i] != ' ' and test[1][i] != '-' and test[1][i] != '.':
                    cpf = cpf + test[1][i]
                    finalList.append[cpf]
            break;
        if(test[0] == "Vulgo"):
            vulgo = ''
            for i in range(len(test[1])):
                if test[1][i] != ' ':
                    vulgo = vulgo + test[1][i]
                    finalList.append[test]
                break;

    return finalList

def file_to_text(file):

    file = docx_to_text(file)
    file = file.split('\n')
    return file


def save_text(savedtext,oldtext):

    for i in range(len(text)):
        if(text[i] != ""):
            savedlist.append(text[i])
    return savedlist

def return_search(text,listtest):
    for i in range(len(text)):
        return

def  format_text(text,formatedtext):
    for i in range(len(text[1])):
       if text[1][i] != ' ' and text[1][i] != '-' and text[1][i] != '.':
            format_text = formatedtext + text
    return format_text
            