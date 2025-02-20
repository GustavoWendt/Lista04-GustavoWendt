#EXE 012 - Você é um desenvolvedor de sistemas trabalhando em um projeto para um salão de beleza. O salão precisa de um sistema para gerenciar os horários de atendimento dos clientes. Primeiro, a dona do salão monta a grade horária da agenda. Depois, uma cliente deseja agendar um horário, e o sistema exibe os horários disponíveis. A dona do salão então agenda o horário escolhido pela cliente, e o horário escolhido não estará mais disponível. O sistema deve continuar permitindo agendamentos até que todos os horários disponíveis sejam preenchidos ou até que a dona do salão decida parar.
#Desenvolva um programa em Python que:
#1.	Solicite à dona do salão para inserir os horários disponíveis na agenda.
#2.	Exiba os horários disponíveis para a cliente.
#3.	Permita que a cliente escolha um horário para agendamento.
#4.	Atualize a agenda marcando o horário escolhido como ocupado.
#5.	Pergunte se deseja agendar mais um horário e continue até que todos os horários estejam preenchidos ou a dona do salão decida parar.
horarios=[]
num=int(input("Quantos horários terá dísponiveis?: "))
for i in range(num):
 disponiveis=input("Digite os horarios(hh/mm): ")
 horarios.append(disponiveis)

print(horarios)

agendamento=input("Digite o horário como está na lista, que deseja marcar: ")

if agendamento in horarios:
 i=horarios.index(agendamento)
 horarios.remove(agendamento)
 print("Horario agendado com sucesso!: ")
 print("Nova lista:",horarios)



novamente=input("Deseja agendar mais um horário?:")
if novamente =='sim':
 agendamento=input("Digite o horário como está na lista, que deseja marcar: ")
 if agendamento in horarios:
  i=horarios.index(agendamento)
  horarios.remove(agendamento)
  print("Horario agendado com sucesso!: ")
  print("Nova lista:",horarios)