from distutils.core import setup
from lib2to3.pgen2.token import VBAR
from xml.etree.ElementInclude import include
from pesquisaNome import *
from pesquisaCPF import *
from pesquisaVulgo import *
from config import *
from tkinter import *
import os
import py2exe

include = []
setup(windows=['main.py','readDocs.py'])