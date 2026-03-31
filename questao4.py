soma_positivos = 0
quantidade_negativos = 0
lista_numeros = []





for i in range(5):
   numero_inteiro = int(input("informe um numero: "))
   lista_numeros.append(numero_inteiro)

   print(lista_numeros)


   for numero_inteiro in lista_numeros:
      if numero_inteiro >= 0:
         soma_positivos = soma_positivos + numero_inteiro
      else:
         quantidade_negativos = quantidade_negativos + 1


         print("a soma dos valores positivos é {0}".format(soma_positivos))
         print(f"a quantidade de valores negativos e {quantidade_negativos}")
         

   




  
