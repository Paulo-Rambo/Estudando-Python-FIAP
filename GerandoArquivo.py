arquivo = open("numeros.txt", "w")
for linha in range(1, 10):
    arquivo.write(f"numero {linha}\n")
arquivo.close()