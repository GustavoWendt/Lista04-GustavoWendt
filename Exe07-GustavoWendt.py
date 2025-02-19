#EXE 007 . Peça ao usuário para inserir seu nome e um número. Se o número for menor que 10, exiba o nome dele esse número de vezes; caso contrário, exiba a mensagem “Numero muito alto" três vezes.
nome=input("Qual o seu nome?: ")
numero=int(input("Digite um número menor que 10: "))
i=0
if numero <10:
 for i in range(numero):
    print(nome)
else:
  for i in range(3):
   print("Número muito alto")
print("Gustavo Wendt")


