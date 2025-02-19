#EXE 008 - Defina uma variável chamada total como 0 (Zero).
#Peça ao usuário para inserir cinco números e, após cada entrada, pergunte se ele deseja que esse número seja incluído (S ou s, N ou n).
#Se ele desejar, adicione o número ao total. Se ele não quiser incluí-lo, não o adicione ao total. Depois de inserir todos os cinco números, exiba o total.
total=0
for i in range(5):
    num=int(input("Digite um número: "))
    resposta=input("Gostaria de incluir esse número ao total(s/n): ".strip().lower())
    if resposta == 's':
      total+=num
print("O total final é: ",total)
print("Gustavo Wendt")