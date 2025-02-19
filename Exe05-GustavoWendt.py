#5.	Peça ao usuário para inserir um número que deseja a tabuada e em seguida exiba a tabuada desse número.
numero=int(input("Digite o número que deseja a tabuada: "))
print("Tabuada do número:",numero,"é:")
for i in range(1,11):
    print(numero,"é:",numero,"x",i,"=", numero *i)
print("Gustavo Wendt")