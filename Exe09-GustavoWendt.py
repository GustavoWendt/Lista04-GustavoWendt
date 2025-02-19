#EXE 009 - Faça um programa que pergunte em qual direção o usuário deseja contar (para cima [ c/C] ou para baixo [a/A]).
#	Se ele selecionar para cima, peça o número superior e conte de 1 até esse número.
#	Se ele selecionar para baixo, peça-lhe para inserir um número abaixo de 20 e, em seguida, faça uma contagem regressiva de 20 até esse número.
#	Se ele inserir algo diferente de cima ou baixo, exiba a mensagem “Direção Invalida!".
direcao=input("Digite a direção( c/C)para cima e (a/A) para baixo: ".strip().lower())
if direcao =='c':
    num=int(input("Digite um número superior a 1: "))
    if num >=1:
      for i in range(1, num +1, +1):
        print(i)
    else:
        print("Direção Invalida!")
if direcao=='a':
    num=int(input("Digite um número inferior a 20: "))
    if num <20:
       for i in range(20, num -1, -1):
        print(i)
    else:
        print("Direção Invalida!")