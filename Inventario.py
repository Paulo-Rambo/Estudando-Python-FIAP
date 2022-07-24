from Funcoes.Funcoes_inventario import *

inventario={}
opcao = menu()

inventario = {}
while opcao>0 and opcao<4:
    if(opcao == 1):
        registrar(inventario)
    elif(opcao == 2):
        persistir("inventario.csv", inventario)
    elif(opcao == 3):
        exibir("inventario.csv")
    opcao = menu()
