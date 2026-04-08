praias = {}
continua = 0 

while continua == 0:

    nome_praia = input("informe o nome da praia: ")
    distancia_centro = float(input("informe a distancia da praia ao centro da cidade em km: "))
    media_veranistas = float(input("informe o numero medio de veranistas na praia: "))
    tipo_acesso = float(input("informe o tipo de acesso a praia (0 - o acesso nao asfaltado; 1 - acesso asfaltado): "))

    praias[nome_praia] = [distancia_centro, media_veranistas, tipo_acesso]

    continua = int(input("\ndeseja cadastrar nova praia (0 - sim / 1 - não): "))
    print()





print(praias)


