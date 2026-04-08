lista_nomes = []
lista_familias = []
qtd_nomes = 3
qtd_familias = 2
for familia in range(2):
    for nome in range(3):
        nome = input("informe um nome de sua familia")
        lista_nomes.append(nome)

        lista_familias.append(lista_nomes)
        lista_nomes = []
for item in lista_familias:

 print(item)
 print()
