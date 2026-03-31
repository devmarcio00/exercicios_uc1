total_loja = 0

for i in range(10):

    nome = input("Nome do cliente: ")
    valor_compra = float(input("Valor da compra: "))

    if valor_compra >= 250:
        desconto = valor_compra * 0.20
    else:
        desconto = valor_compra * 0.15

    valor_pagar = valor_compra - desconto

    print("Nome:", nome)
    print("Valor da compra:", valor_compra)
    print("Desconto:", desconto)
    print("Valor a pagar:", valor_pagar)

    total_loja += valor_pagar

print("Total arrecadado pela loja:", total_loja)