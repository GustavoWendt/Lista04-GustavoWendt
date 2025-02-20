
horarios = []


num = int(input("Quantos horários estarão disponíveis?: "))


for _ in range(num):
 disponivel = input("Digite o horário (hh:mm): ").strip()
 horarios.append(disponivel)


print("\nHorários disponíveis:", horarios)


for _ in range(len(horarios)): 
 if not horarios:
  print("\nTodos os horários foram preenchidos. Encerrando o sistema.")
 break

agendamento = input("\nDigite o horário que deseja marcar (como está na lista): ").strip()

if agendamento in horarios:
 horarios.remove(agendamento)
 print("Horário agendado com sucesso!")
 print("Horários restantes:", horarios)
else:
 print("Horário inválido ou já preenchido. Tente novamente.")


novamente = input("\nDeseja agendar mais um horário? (sim/não): ").strip().lower()
if novamente not in ["sim", "s"]:
 print("Encerrando o sistema de agendamentos.")


print("Gustavo Wendt")