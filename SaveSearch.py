from importlib.resources import path
from operator import truediv
import os
import glob
import io

def list_files_docs_in(path,docs):

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