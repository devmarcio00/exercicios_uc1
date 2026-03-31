soma_positivos = 0
quantidade_negativos = 0

for i in range(5):
    numero_inteiro = int(input("Informe um número: "))
  
    if numero_inteiro >= 0:
        soma_positivos += numero_inteiro
    else:
        quantidade_negativos += 1

print("A soma dos valores positivos é {0}".format(soma_positivos))
print(f"A quantidade de valores negativos é {quantidade_negativos}")

