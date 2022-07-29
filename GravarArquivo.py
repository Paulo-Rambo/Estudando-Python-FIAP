with open("teste.txt", "w") as arquivo:
    conteudo = arquivo.write("É fácil comer pamonha em São Paulo!\n")

with open("teste.txt", "a") as arquivo:
    conteudo = arquivo.write("É fácil adicionar mais linhas!")
