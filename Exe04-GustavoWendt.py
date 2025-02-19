#4.	Escreva um programa para pedir um número e em seguida o nome. Exiba o nome (uma letra de cada vez em cada linha). E repita isso para o número de vezes que ele digitou.
nome=input("Qual o seu nome?: ")
numero=int(input("Digite um número qualquer"))
for i in range(numero):
    for letras in nome:
     print(letras)
print("Gustavo Wendt")