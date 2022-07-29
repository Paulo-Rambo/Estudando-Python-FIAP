from Funcoes.Funcoes_inventario import *


opcao = menu()

inventario = {}
while opcao>0 and opcao<4:
    if(opcao == 1):
        registrar(inventario)
    elif(opcao == 2):
        persistir("inventario.csv", inventario)
    elif(opcao == 3):
        texto = exibir("inventario.csv")
        for linha in texto:
            linhaSeparada = linha.split(";")
            print("Data de atualização:", linhaSeparada[0])
            print("Descrição:", linhaSeparada[1])
            print("Departamento:", linhaSeparada[2])

            # print(linha.find(";")) #find acha o índice
            # print(linha[linha.find(";"): -1]) #colocando o indice do find no slice, jeito mais facil
            # print(linha[slice(linha.find(";"), -1)]) #jeito mais enrrolado
            # print(linha[2:-1]) #slice apenas, jeito mais fácil
            #print(linha[slice(2, -1)]) #slice apenas
            # ou print(linha[2:-1])

            #PRATICANDO SLICE E FIND

            #separaItens = linha[linha.find(";")+1: -1]
            #dataAtualizacao = separaItens[0: separaItens.find(";")]
            #separaItens = separaItens[separaItens.find(";")+1: -1]
            #descricao = separaItens[0: separaItens.find(";")]
            #departamento = linha[linha.rfind(";")+1: -1]

            #print("Data de atualização:", dataAtualizacao)
            #print("Descrição:", descricao)
            #print("Departamento:", departamento)

    opcao = menu()
