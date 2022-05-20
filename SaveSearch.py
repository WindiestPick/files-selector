from distutils.log import Log
from importlib.resources import path
from SaveSearch import *
from operator import truediv
import os
import glob
import io

from Search import in_file_search

def list_files_docs_in(path):

    os.chdir(path[0])
    docs = glob.glob("*.*")
    docs = return_docs(docs)
    os.chdir(path[2])
    return docs

def return_docs(docs):

    for i in docs:
        if(verify_if_file_is_docx[i] == True): docs.apprend(i) 
    return docs

def return_no_docs(file):
    for i in file:
        if(verify_if_file_is_docx[i] == False): file.apprend(i) 
    return file

def verify_if_file_is_docx(file):

    if(file[1] == ".doc" or file[1] == ".docx"): 
        return True
    else: 
        return False

def search_in_doc(path, search):
    files = list_files_docs_in(path)
    arq = get_cache(search,path[2])
    if arq == "":
        set_cache(update_cache(path,files,search))
    return arq


def update_cache(path,files,search):
    for i in range(len(files)):
        Arq = in_file_search(path[1] + files[i])
        if (search == Arq):
            set_cache(search, files[i], path[2])
                


def get_cache(search,path):
    cachelog = save_lines(path)
    cachelog = return_file_cache(search,cachelog)
    return cachelog

def save_lines(path):
    cachelog = io.open(path + "logSeach.txt", "r", encoding="utf-8")
    cachelog = cachelog.readlines()
    cachelog.close()
    return cachelog

def return_file_cache(search,cachelog):
    for i in range(len(cachelog)):
        searchArq = cachelog[i].split(":")
        if searchArq[0] == search:
            return searchArq[1].replace('\n', '')
    return ""


def set_cache(search, nameArq, path):
    log = io.open(path + "logCpf.txt","a", encoding="utf-8")
    log.write("\n"+search + ':' + nameArq)
    log.close()
    return 

def open_write_close_arq(log):
    log = io.open("logCpf.txt", "w")
    log.write("")
    log.close()
    return Log

