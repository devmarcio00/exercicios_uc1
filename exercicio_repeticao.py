class Candidato:
    
 def __init__(self, nome, nota_portugues, nota_matematica, nota_conhecimentos_gerais):

     self.nome = nome
     self.nota_portugues = nota_portugues
     self.nota_matematica = nota_matematica
     self.nota_conhecimentos_gerais = nota_conhecimentos_gerais
     self.media = 0.0
     self.situacao = "reprovado"
def __str__(self):
  return f"{nome}"

# programa principal
Candidatos = []

continua = 0
while continua == 0:
  
nome = input("informe o nome do candidato: ")
nota_port = float(input("informe a nota de portugues: "))
nota_mat = float(input("informe a nota de matematica: "))
nota_conhec = float(input("informe a nota de conhecimento gerais: "))

# inserindo no dicionario o nome do candidato e lista de dados como value/valor

Candidatos = Candidato(nome, nota_port, nota_mat, nota_conhec)

candidatos.append(Candidato)

#pergunto se deseja continuar a cadastrar novo aluno 
continua = int(input("\nDeseja cadastrar novo candidato (0 - sim / qualquer outro numero - não)"))
print()


print(Candidatos)