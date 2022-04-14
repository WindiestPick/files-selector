from pesquisaNome import PesquisaNome
path = "D:\\"

pesquisa = input("digite o nome do arquivo: ")

lista = PesquisaNome(pesquisa, path)
for i in range(len(lista)):
    print( i ," - ", lista[i])