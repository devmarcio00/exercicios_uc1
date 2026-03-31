valor = float(input("Digite o valor do produto: "))

if valor <= 5000:
    desconto = valor * 0.20
else:
    desconto = valor * 0.15

valor_final = valor - desconto

print("Valor original:", valor)
print("Desconto:", desconto)
print("Valor final:", valor_final)