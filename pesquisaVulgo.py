from importlib.resources import path
import os
import glob
import io
from readDocx import GetVulgo


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
    vulgoArq = ""
    print("search_vulgo no INICIO")
    print(files)
    arq = get_vulgo_cache(vulgo, path[2])
    print("arq do seach vulgo DEPOIS INICIO")
    print(arq)
    if arq == "":
        for i in range(len(files)):
            vulgoArq = GetVulgo(path[1] + files[i])
            print("vulgo arqa baixo:")
            print("|||"+vulgoArq +"||||"+ vulgo+"|||fas")
            if (vulgo == vulgoArq):
                set_vulgo_cache(vulgo, files[i], path[2])
                print("FILESSS DO SEARCH")
                print(files[i])
                return files[i]
    else:

        print("VULGO a baixo (DO RETURN)")
        print(arq)
        return arq


def get_vulgo_cache(vulgo, path):
    log = io.open(path + "logVulgo.txt", "r", encoding="utf-8")
    print(log)
    vulgoList = log.readline()
    print(vulgoList)
    for i in range(len(vulgoList)):
        vulgoArq = vulgoList[i].split(":")
        if(vulgoArq[0] == vulgo):
            log.close()
            print(vulgoArq[1])
            return vulgoArq[1].replace('\n', '')
        log.close()
        return ""


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
        vulgoArq = GetVulgo(path[1] + files[1])
        set_vulgo_cache(vulgoArq, files[i], path[2])
