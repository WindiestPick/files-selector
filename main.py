from pesquisaNome import PesquisaNome
path = "C:\\Users\\Marketing\\Documents\\Teste\\"

pesquisa = input("digite o nome do arquivo: ")

lista = PesquisaNome(pesquisa, path)
for i in range(len(lista)):
    print( 1 ," - ", lista[i])