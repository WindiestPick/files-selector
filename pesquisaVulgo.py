from importlib.resources import path
import os
import glob
import io
from readDocx import GetVulgo
from formatStr import formata


def list_files_in(path):
    os.chdir(path[0])
    files = glob.glob('*.docx')
    lst = glob.glob('*.doc')
    for i in lst:
        files.append(i)
    os.chdir(path[2])
    return files

def search_vulgo(path,vulgo):
    files = list_files_in(path)
    returnList = []
    vulgoArq = ''
    vulgo = vulgo.replace(" ", "")
    vulgo = formata(vulgo)
    arq = get_vulgo_cache(vulgo, path[2])
    if arq == []:
        for i in range(len(files)):
            vulgoArq = GetVulgo(path[1] + files[i])
            vulgoArq = formata(vulgoArq)
            if (vulgo.lower() == vulgoArq.lower()):
                set_vulgo_cache(vulgo, files[i], path[2])
                returnList.append(files[i])
        return returnList
    else:
        return arq


def get_vulgo_cache(vulgo, path):
    log = io.open(path + "logVulgo.txt", "r", encoding="utf-8")
    returnList = []
    vulgoList = log.readlines()
    #vulgo = vulgo.replace(" ","")  -Já tem um lá em cima
    for i in range(len(vulgoList)):
        vulgoArq = vulgoList[i].split(":")
        compara = formata(vulgoArq[0])
        if(compara.lower() == vulgo.lower()):
            returnList.append(vulgoArq[1].replace('\n', ''))
    log.close()
    return returnList


def set_vulgo_cache(vulgo, nameArq, path):
    log = io.open(path + "logVulgo.txt", "a", encoding="utf-8")
    log.write("\n" + vulgo + ":" + nameArq)
    log.close()

def update_cache(path):
    files = list_files_in(path)
    log = io.open("logVulgo.txt", "w")
    log.write("")
    log.close()
    for i in range(len(files)):
        vulgoArq = GetVulgo(path[1] + files[i])
        set_vulgo_cache(vulgoArq, files[i], path[2])