#2.	Faça um programa que solicite ao usuário para digitar o seu nome e um número qualquer, em seguida exiba o seu nome varias vezes de acordo com o número que ele digitou.
nome=input("Qual o seu nome?: ")
numero=int(input("Digite um número qualquer"))
i=0
for i in range(numero):
    print(nome)
print("Gustavo Wendt")