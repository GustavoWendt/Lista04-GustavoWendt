#EXE 010 - Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
#	Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
#	Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".
qtde_pessoas=int(input("Quantas pessoas serão comvidadas?: "))
if qtde_pessoas <10:
    for i in range(qtde_pessoas):
        nome=input("Diga o nome do convidado(a): ")
        print(nome,"Está convidado para a festa!:" )
else:
    print("Muitos convidados! ")
print("Gustavo Wendt ")