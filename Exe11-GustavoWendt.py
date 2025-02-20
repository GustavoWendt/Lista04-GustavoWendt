#EXE 011 - Você é um desenvolvedor de sistemas trabalhando em um projeto colaborativo com sua equipe.
#Para garantir que todas as tarefas do projeto sejam concluídas dentro do prazo, você decide criar um pequeno programa para controlar o status das tarefas.
#O programa deve permitir que você insira o nome de cada tarefa e indique se ela está concluída ou não.
#No final, o programa deve apresentar um resumo com o total de tarefas, quantas estão concluídas e quantas ainda estão pendentes.
#Desenvolva um programa em Python que:
#1.	Solicite ao usuário o número de tarefas a serem inseridas.
#2.	Para cada tarefa, solicite o nome da tarefa e se ela está concluída (aceitando "sim", "s", "não" ou "n").
#3.	Conte e exiba o número de tarefas concluídas e não concluídas.
numero_tarefas=int(input("Quantas tarefas serão iseridas?: "))
sim=0
nao=0
for i in range(numero_tarefas):
 tarefas=input("Digite uma tarefa: ")
 comprida_ou_nao=input("Esta tarefa está comprida ou está pendente?9sim/s,não/n): ".strip().lower())
 if comprida_ou_nao in ['s', 'sim']:
  sim+=1
 elif comprida_ou_nao in ['n', 'nao', 'não']:
  nao+=1
 else:
  print("Dados inválidos! tente novamente!: ")
  print("Gustavo Wendt ")

print("Existem",numero_tarefas,"de tarefas inseridas: ")
print("Existem",sim,"de tarefas concluidas: ")
print("Existem",nao,"de tarefas pendentes: ")
print("Gustavo Wendt ")