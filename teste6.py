total_alunos = int(input("Digite o número de alunos: "))

cont_menos_10 = 0
cont_entre_10_15 = 0
cont_acima_15 = 0

for i in range(total_alunos):
    vezes = int(input(f"Quantas vezes o aluno {i+1} usou o restaurante? "))

    if vezes < 10:
        cont_menos_10 += 1
    elif 10 <= vezes <= 15:
        cont_entre_10_15 += 1
    else:
        cont_acima_15 += 1

perc_menos_10 = (cont_menos_10 / total_alunos) * 100
perc_acima_15 = (cont_acima_15 / total_alunos) * 100

print(f"Percentual que usaram menos de 10 vezes: {perc_menos_10:.2f}%")
print(f"Percentual entre 10 e 15 vezes: {perc_entre_10_15:.2f}%")
print(f"Percentual acima de 15 vezes: {perc_acima_15:.2f}%")