import minhas_classes as m 


meucao = m.Cao(10, "poodle")
peso = meucao.peso
raca = meucao.raca
print( f"meu{raca} pesa {peso} kg")
meucao.latir()

meu_outro_cao = m.Cao(12, "labrador")
print( f "meu outro cão é um {meu_outro_cao.raca} e pesa {meu_outro_cao.peso} kg")
meu_outro_cao.latir()

print(meucao)
print(meu_outro_cao)

meu_golden = m.golden(15, "creme claro")
peso = meu_golden.peso
raca = meu_golden.raca
cor_pelo = meu_golden.cor_pelo
print( f"meu {raca} pesa {peso} kg e tem pelo da cor {cor_pelo}")
meu_golden.latir()
meu_golden.sentar()
      
