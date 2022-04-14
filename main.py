from pesquisaNome import PesquisaNome
from pesquisaCPF import PesquisaCPF
import os

path = ["C:\\Users\\Marketing\\Documents\\Teste","C:\\Users\\Marketing\\Documents\\Teste\\"]

pesquisa = input("digite o nome da pessoa: ")

lista = PesquisaNome(pesquisa, path[0])
for i in range(len(lista)):
    print( i+1 ," - ", lista[i])

pesquisa = input("digite o cpf que deseja pesquisar: ")

print(PesquisaCPF(path,pesquisa))