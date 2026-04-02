menos_10 = 0
entre_10_15 = 0
mais_15 = 0
total = 0
while True:
    uso = int(input("Digite o número de vezes (ou -1 para sair): "))

    if uso == -1:
        break

    total += 1

    if uso < 10:
     menos_10 += 1
    elif 10 <= uso <= 15:
        entre_10_15 += 1
    else:
        mais_15 += 1

# cálculo depois do loop
if total > 0:
    p1 = (menos_10 / total) * 100
    p2 = (entre_10_15 / total) * 100
    p3 = (mais_15 / total) * 100

    print("Menos de 10:", f"{p1:.2f}%")
    print("Entre 10 e 15:", f"{p2:.2f}%")
    print("Mais de 15:", f"{p3:.2f}%")
else:
    print("Nenhum aluno foi informado.")