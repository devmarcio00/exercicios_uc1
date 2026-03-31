ganhos =float(input("digite o total de ganhos em R$:"))

if ganhos <= 500.00:
    impostos = 0.
  
elif ganhos <= 1500.00:
    impostos = ganhos * 0.10
   

elif ganhos <= 2500.00:
    impostos = ganhos * 0.15
    
else: 
    impostos = ganhos * 0.20
    
print("o valor do desconto é: ", impostos)

    