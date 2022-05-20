from logging.config import listen
import os
import glob
from ReadDocx import *

def name_search(text,path):
    os.chdir(path[0])
    files = glob.glob( '*'+ text +'*.*')
    os.chdir(path[2])
    return files


def in_file_search(file):
    textfile = file_to_text(file)
    savedlist = []
    savedlist = save_text(savedlist,textfile)
    savedlist =  work_list(savedlist)
    return savedlist

def work_list(savedlist):
    newtest =  []
    for i in range(len(savedlist)):
        test = formating_with_slip(savedlist[i])
        newtest.append(analise_search(test))
    return newtest


def file_to_text(file):
    file = docx_to_text(file)
    file = file.split('\n')
    return file


def save_text(savedfiletext,oldfiletext):
    for i in range(len(oldfiletext)):
        if(oldfiletext[i] != ""):
            savedfiletext.append(oldfiletext[i])
    return savedfiletext


def formating_with_slip(savedlist):
    for i in range(len(savedlist)):
        test = savedlist[i]
        test = test.split(":")
    return test

def analise_search(test):
    if(test[0] == "Vulgo" or "CPF" or "nome completo"or "Nome completo" or "nome Completo"):
        formated = format_text(test)
    return formated


def  format_text(text):
    
    for i in range(len(text[1])):
        format_text = ""
        if text[1][i] != ' ' and text[1][i] != '-' and text[1][i] != '.':
            format_text = format_text + text[1][i]; break;
    return format_text


