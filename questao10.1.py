
n = int(input("Quantas praias deseja cadastrar? "))

# (a) contador de praias com mais de 15 km
contador_distancia = 0

# (b) soma e contador para média (acesso não asfaltado)
soma_veranistas = 0
contador_nao_asfaltado = 0

print("\n--- Cadastro das praias ---\n")

# Loop para ler os dados de cada praia
for i in range(n):

    print(f"Praia {i+1}:")

    # Entrada de dados
    nome = input("Nome da praia: ")
    distancia = float(input("Distância do centro (km): "))
    veranistas = int(input("Número de veranistas: "))
    acesso = int(input("Tipo de acesso (0 - não asfaltado | 1 - asfaltado): "))

    print()  # só para organizar a saída

    # =========================
    # (a) Praias com mais de 15 km
    # =========================
    if distancia > 15:
        contador_distancia += 1

    # =========================
    # (b) Média de veranistas (acesso não asfaltado)
    # =========================
    if acesso == 0:
        soma_veranistas += veranistas
        contador_nao_asfaltado += 1

    # =========================
    # (c) Praias asfaltadas com menos de 1000 veranistas
    # =========================
    if acesso == 1 and veranistas < 1000:
        print("Praia com acesso asfaltado e menos de 1000 veranistas:")
        print(f"Nome: {nome} | Distância: {distancia} km\n")


# =========================
# Cálculo da média (b)
# =========================
if contador_nao_asfaltado > 0:
    media = soma_veranistas / contador_nao_asfaltado
else:
    media = 0  # evita divisão por zero

# =========================
# Resultados finais
# =========================
print("\n--- Resultados ---\n")

print("a) Número de praias a mais de 15 km:", contador_distancia)

print("b) Média de veranistas (acesso não asfaltado):", media)