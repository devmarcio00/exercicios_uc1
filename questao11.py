# Criamos uma variável chamada soma e iniciamos com 0
# Ela vai guardar o resultado final da soma de todos os termos
soma = 0

# Usamos um laço for que vai de 1 até 8 (inclusive)
# O range(1, 9) gera os números: 1, 2, 3, ..., 8
# Cada número representa a posição do termo na PG
for i in range(1, 9):

    # Calculamos o termo da PG usando potência
    # Como a PG é: 3, 9, 27, 81...
    # Cada termo é 3 elevado a i (3^i)
    termo = 3 ** i

    # Somamos o termo atual à variável soma
    # Isso acumula os valores ao longo do loop
    soma = soma + termo

# Após o fim do loop, mostramos o resultado final
print("Soma da PG:", soma)













# Criamos a variável soma e iniciamos com 0
# Ela vai acumular o total dos termos da PG
soma = 0

# Criamos a variável termo e iniciamos com 3
# Esse é o primeiro termo da progressão geométrica
termo = 3

# Enquanto o termo for menor ou igual a 6561, o loop continua
# Isso garante que o último termo (6561) será incluído
while termo <= 6561:

    # Somamos o valor atual do termo à variável soma
    # A cada repetição, acumulamos mais um valor
    soma = soma + termo

    # Atualizamos o termo para o próximo da PG
    # Como a razão é 3, multiplicamos o termo atual por 3
    termo = termo * 3

# Quando o termo passar de 6561, o loop para
# Agora mostramos o resultado final
print("Soma da PG:", soma)