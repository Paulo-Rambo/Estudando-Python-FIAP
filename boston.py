# Qual o total de passageiros nos vôos internacionais que partiram do aeroporto de Logan em 2014?

with open("economic-indicators.csv", "r") as listaBoston:
    anoDesejado = int(input("Digite o ano para saber o numero de passageiros que passaram pelo aeroporto de Logan: \n"))
    anoDesejadoDiaria = int(input("Digite o ano desejado para saber o mês com maior média de diaria nos hotéis: \n"))
    numeroTotal2014 = 0
    numeroMaior = 0
    maiorMediaDiaria = 0
    mesMaiorMediaDiaria = []
    numeroNoAnoDesejado = 0
    for itemDaLista in listaBoston.readlines()[1:-1]:
        itemLocal = itemDaLista.split(",")
        if itemLocal[0] == "2014":
            numeroTotal2014 = float(itemLocal[3]) + numeroTotal2014
        if float(itemLocal[2]) > float(numeroMaior):
            maiorTransito = itemLocal
            numeroMaior = float(itemLocal[2])
        if float(itemLocal[0]) == anoDesejado:
            numeroNoAnoDesejado += float(itemLocal[2])
        if float(itemLocal[0]) == anoDesejadoDiaria:
            if maiorMediaDiaria < float(itemLocal[5]):
                maiorMediaDiaria = float(itemLocal[5])
                mesMaiorMediaDiaria = itemLocal[1]

    print("O total de passageiros em vôos internacionais em 2014 é", numeroTotal2014)
    print("O mês/ano que ocorreu o maior trânsito foi:", maiorTransito[1], "e", maiorTransito[0])
    print("O número de passageiros no ano de ", anoDesejado, "foi", numeroNoAnoDesejado)
    print("O mês com maior média diária nos hotéis no ano escolhidoi foi o mês: ", mesMaiorMediaDiaria)




