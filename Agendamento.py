from collections import deque

class Agendamento:
  def add(self, nome, CPF, c_sus, c_residencia, fila_externa):
    self.nome = nome
    self.c_sus = c_sus
    self.c_residencia = c_residencia
    self.CPF = CPF
    fila_externa.append(self)
    print(f"{self.nome} agora está na fila")

  def __str__(self):
    return f"Agendamento(Nome: {self.nome}, CPF: {self.CPF}, C_SUS: {self.c_sus}, C_Residencia: {self.c_residencia})"

  def mostrar_fila(self):
    if fila_global:
      print("\n fila atual:",list(fila_global))
    else:
      print("\n Nenhuma pessoa na fila")

fila_global = deque()

while True:

  gerenciador_agendamentos = Agendamento()

  entrada_nome = input("Digite seu nome: ")
  entrada_CPF = input("Digte seu CPF: ")
  entrada_c_sus = input("Digite seu C_SUS: ")
  entrada_c_residencia = input("Digite seu C_RESIDENCIA: ")

  gerenciador_agendamentos.add(entrada_nome, entrada_CPF, entrada_c_sus, entrada_c_residencia, fila_global)

  print("Estado atual da fila:")
  for mostrar_fila in fila_global:
      print(mostrar_fila)

  outro_agendamento = input("Deseja adicionar outra pessoa? (s/n)")
  if outro_agendamento != "s":
    print("Encerrando, até a proxima")
    break