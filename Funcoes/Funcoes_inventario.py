def exibir(arquivo):
    with open(arquivo, "r") as inv:
        print(inv.readlines())

def persistir(arquivo, inventario):
    with open(arquivo, "a") as inv:
        for chave, valor in inventario.items():
            inv.write(chave + ";" + valor[0] + ";" +
                      valor[1] + ";" + valor[2] + "\n")
            print("Persistido com sucesso!")

def registrar(inventario):
    resp="S"
    while resp=="S":
        inventario[input("Digite o número patrimonial: ")]=[
        input("Digite a data da última atualização: "),
        input("Digite a descrição: "),
        input("Digite o departamento: ")]
        resp=input("Digite <S> para continuar.").upper()

def menu():
    opcao = int(input("Digite: \n"
                      "<1> para registrar ativo\n"
                      "<2> para persistir em arquivo\n"
                      "<3> para exibir ativos armazenados\n"))
    return opcao