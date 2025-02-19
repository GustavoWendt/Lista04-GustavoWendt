#6.	Peça um número abaixo de ‘50’ e em seguida faça uma contagem regressiva até esse número, certificando-se que eles inseriram na saída
numero= int(input("Digite um número abaixo de '50': "))
if numero <50:
    print("Número inválido, tente novamente: ")
    for i in range(50, numero -1, -1):
        print(i)
    else:
        print("O número digitado tem que ser inferior a 50!")
print("Gustavo Wendt")