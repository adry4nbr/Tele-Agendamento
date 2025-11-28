# Mudança == Troca na busca de agendamento: ID por CPF
from collections import deque # Importa a classe deque para gerenciar a fila de agendamentos
from time import sleep # Importa a função sleep para pausar a execução do programa
import random # Importa a biblioteca random para gerar números aleatórios

class Agendamento:
  fila = deque() # Fila estática (da classe) para armazenar todos os agendamentos
  proximo_id = 1 # ID estático (da classe) para atribuir um ID único a cada novo agendamento

  def __init__(self, nome, cpf, c_sus, c_residencia, telefone, data_agendamento, tipo_agendamento): # Método construtor para inicializar um novo objeto Agendamento
    self.cpf = cpf # Atribui o CPF ao agendamento
    self.agendamento_id = Agendamento.proximo_id # Atribui o próximo ID disponível ao agendamento
    self.nome = nome # Atribui o nome ao agendamento
    self.c_sus = c_sus # Atribui o Cartão SUS ao agendamento
    self.c_residencia = c_residencia # Atribui o Cartão de Residência ao agendamento
    self.telefone = telefone # Atribui o telefone ao agendamento
    self.data_agendamento = data_agendamento # Atribui a data do agendamento
    self.tipo_agendamento = tipo_agendamento # Atribui o tipo de agendamento

    Agendamento.proximo_id += 1 # Incrementa o contador de ID para o próximo agendamento

  def __str__(self): # Método para retornar uma representação em string do objeto Agendamento
    return f"Agendamento {self.agendamento_id} (Nome: {self.nome}, CPF: {self.cpf}, C_SUS: {self.c_sus}, C_Residencia: {self.c_residencia}, Telefone: {self.telefone}, Data do Agendamento: {self.data_agendamento}, Tipo de agendamento: {self.tipo_agendamento})"

  @classmethod # Decorador para definir um método de classe
  def add(cls, nome, cpf, c_sus, c_residencia, telefone, data_agendamento, tipo_agendamento): # Método de classe para adicionar um novo agendamento à fila (CREATE)
    novo_agendamento = cls(nome, cpf, c_sus, c_residencia, telefone, data_agendamento, tipo_agendamento) # Cria uma nova instância de Agendamento
    cls.fila.append(novo_agendamento) # Adiciona o novo agendamento ao final da fila
    sleep(1.5) # Pausa por 1.5 segundos
    print(f'{novo_agendamento.nome} foi agendado com sucesso!') # Informa que o agendamento foi adicionado
    sleep(1.5) # Pausa por 1.5 segundos
    return

  @classmethod
  def checar_agendamento(cls, numero_agendamento): # Método de classe para verificar um agendamento pelo ID (READ específico)
    for fila_agendamento in cls.fila: # Itera sobre cada agendamento na fila
      if fila_agendamento.cpf == numero_agendamento: # Se o ID do agendamento corresponder
        print(fila_agendamento) # Imprime os detalhes do agendamento encontrado
        print(f"{fila_agendamento.nome} está agendado")
        print('='*30)
        sleep(1.5)
        return

    # Se chegarmos aqui, o ID não foi encontrado após verificar todos os agendamentos
    print(f'Não foi encontrado nenhum agendamento com o ID indicado.')
    print('='*30)
    sleep(1.5)

  @classmethod
  def atualizar(cls, numero_agendamento, novo_nome, novo_cpf, novo_c_sus, novo_c_residencia, novo_telefone, novo_data_agendamento, novo_tipo_agendamento): # Método para atualizar um agendamento (UPDATE)
    for agendamento in cls.fila: # Itera sobre cada agendamento na fila
      if agendamento.cpf == numero_agendamento: # Se o ID do agendamento corresponder

        nome_antigo = agendamento.nome # Armazena o nome antigo para exibição

        # Realiza a Atualização dos atributos
        agendamento.nome = novo_nome # Atualiza o nome
        agendamento.cpf = novo_cpf # Atualiza o CPF
        agendamento.c_sus = novo_c_sus # Atualiza o Cartão SUS
        agendamento.c_residencia = novo_c_residencia # Atualiza o Cartão de Residência
        agendamento.telefone = novo_telefone # Atualiza o telefone
        agendamento.data_agendamento = novo_data_agendamento # Atualiza a data do agendamento
        agendamento.tipo_agendamento = novo_tipo_agendamento # Atualiza o tipo de agendamento

        sleep(1.5)
        print('='*30)
        print(f" Agendamento {numero_agendamento} de {nome_antigo} atualizado para:")
        print(agendamento) # Imprime os detalhes do agendamento atualizado
        print('='*30)
        sleep(1.5)
        return

    # Se chegar aqui, o ID não foi encontrado
    sleep(1.5)
    print('='*30)
    print(f'Não foi encontrado nenhum agendamento com o ID {numero_agendamento} para atualizar.')
    print('='*30)
    sleep(1.5)

  @classmethod # Decorador para definir um método de classe
  def remover(cls, numero_agendamento): # Método de classe para remover um agendamento pelo ID (DELETE)
    if not cls.fila: # Verifica se a fila está vazia
      print('Não há agendamentos para remover.')
      print('='*30)
      sleep(1.5)
      return

    found = False # Flag para indicar se o agendamento foi encontrado
    nova_fila = deque() # Cria uma nova fila vazia
    agendamento_removido = None # Variável para armazenar o agendamento removido

    for agendamento in cls.fila: # Itera sobre os agendamentos na fila atual
      if agendamento.agendamento_id == numero_agendamento and not found: # Se o ID corresponder e ainda não foi encontrado
        agendamento_removido = agendamento # Armazena o agendamento a ser removido
        found = True # Marca como encontrado para não remover outros com o mesmo ID
      else: # Se não for o agendamento a ser removido ou já foi encontrado
        nova_fila.append(agendamento) # Adiciona o agendamento à nova fila

    if found: # Se o agendamento foi encontrado e removido
      cls.fila = nova_fila # Substitui a fila antiga pela nova (sem o agendamento removido)
      print(f'Agendamento {agendamento_removido.agendamento_id} de {agendamento_removido.nome} removido com sucesso!')
      print('='*30)
      sleep(1.5)
    else: # Se o agendamento não foi encontrado
      print(f'Não foi encontrado nenhum agendamento com o ID {numero_agendamento} para remover.')
      print('='*30)
      sleep(1.5)

# Pra ficar algumas pessoas aleatórias adicionadas no sistema (inicialização) ===============================
p1 = Agendamento.add("Fernando da Silva", 1, 1111111, 1111111, 1111111, "31/12/2026", "Cardiologista")
p2 = Agendamento.add("Alicia Costa", 2, 2222222, 2222222, 2222222, "30/09/26", "Neurologista")
p3 = Agendamento.add("Felicia de Melo", 3, 33333333, 33333333, 33333333, "10/02/27", "Pediatra")
#=============================================================================================================

while True: # Loop principal do menu do programa
  print("--------- Menu Principal ---------")
  print("1. Fazer agendamento")
  print("2. Checar agendamento")
  print("3. Remover agendamento")
  print("4. Atualizar agendamento")
  print("0. Sair do sistema")

  try: # Inicia um bloco para tratamento de erros
    opcao = int(input("Escolha a opção: ").strip())
  except ValueError: # Captura o erro se o usuário não digitar um número
    print("Opção inválida. Por favor, digite um número.")
    sleep(1)
    continue

  if opcao == 1:
    print('-'*30)
    print(f'Area de agendamento. Preencha os dados a seguir.')
    try:
      nomeInput = str(input("Nome: "))
      cpfInput = int(input("CPF (apenas números): "))
      c_susInput = int(input("Número do cartão do SUS (apenas números): "))
      c_residenciaInput = int(input("Número da residência (apenas números): "))
      telefoneInput = int(input("Número de telefone (apenas números): "))
      dia_random = random.randint(1 ,28) # Gera um dia aleatório para a data do agendamento
      mes_random = random.randint(1 ,12) # Gera um mês aleatório para a data do agendamento
      ano_random = random.randint(2025, 2030) # Gera um ano aleatório para a data do agendamento
      data_agendamento = (f"{dia_random}/{mes_random}/{ano_random}") # Formata a data de agendamento
      while True:
        print("--------- Tipos de Agendamentos ---------")
        print("1. Cardiologista")
        print("2. Ortopedista")
        print("3. Pediatra")
        print("4. Oftalmologista")
        print("5. Neurologista")
        print("6. Clínico Geral")

        try:
          tipo = int(input("Escolha qual o tipo de agendamento.").strip())
        except ValueError: # Captura o erro se o usuário não digitar um número
          print("Não temos esse tipo de agendamento. Digite um número.")
          sleep(1)
          continue

        if tipo == 1:
          tipo = "Cardiologista" # Define o tipo de agendamento como Cardiologista
          break
        elif tipo == 2:
          tipo = "Ortopedista" # Define o tipo de agendamento como Ortopedista
          break
        elif tipo == 3:
          tipo = "Pediatra" # Define o tipo de agendamento como Pediatra
          break
        elif tipo == 4:
          tipo = "Oftalmologista" # Define o tipo de agendamento como Oftalmologista
          break
        elif tipo == 5:
          tipo = "Neurologista" # Define o tipo de agendamento como Neurologista
          break
        elif tipo == 6:
          tipo = "Clínico Geral" # Define o tipo de agendamento como Clínico Geral
          break
        else:
          print("Tipo inválido, tente novamente.")
      tipo_agendamentoInput = tipo # Atribui o tipo de agendamento selecionado
      print('-'*30)
      Agendamento.add(nomeInput, cpfInput, c_susInput, c_residenciaInput, telefoneInput, data_agendamento, tipo_agendamentoInput) # Chama o método para adicionar o agendamento
    except ValueError:
      print("Entrada inválida para CPF, SUS, Residência ou Telefone. Por favor, digite apenas números.")
      sleep(1.5)

  elif opcao == 2: # Se a opção for 2 (Checar agendamento)
    print('='*30)
    sleep(1)
    if not Agendamento.fila: # Verifica se a fila está vazia
      print(f'Não há agendamentos marcados.')
      print('='*30)
      sleep(1.5)
    else: # Se a fila não estiver vazia
      print(f'Para checar um agendamento é preciso o CPF do indivíduo.')
      try: # Adiciona tratamento de erro para a entrada do ID
        cpf_agendamento = int(input("Digite o CPF: "))
        print('='*30)
        sleep(1.5)
        Agendamento.checar_agendamento(cpf_agendamento) # Chama o método para checar o agendamento
      except ValueError: # Captura o erro se o usuário não digitar um número
        print("Entrada inválida. O CPF deve ser apenas números. Tente novamente.")
        sleep(1.5)

  elif opcao == 3: # Se a opção for 3 (Remover agendamento)
    print('='*30)
    sleep(1)
    if not Agendamento.fila: # Verifica se a fila está vazia
      print('Não há agendamentos para remover.')
      print('='*30)
      sleep(1.5)
    else: # Se a fila não estiver vazia
      print(f'É necessário informar o CPF do indivíduo que deseja remover o agendamento.')
      try: # Adiciona tratamento de erro para a entrada do ID
          cpf_agendamento = int(input("Digite o CPF: "))
          print('='*30)
          sleep(1.5)
          Agendamento.remover(cpf_agendamento) # Chama o método para remover o agendamento
      except ValueError: # Captura o erro se o usuário não digitar um número
          print("Entrada inválida. O CPF deve ser apenas números. Tente novamente.")
          sleep(1.5)

  elif opcao == 4: # Se a opção for 4 (Atualizar agendamento - UPDATE)
    print('='*30)
    sleep(1)

    # Verifica se a fila de agendamentos está vazia antes de tentar atualizar
    if not Agendamento.fila: # Se a fila estiver vazia
      print(f'Não há agendamentos para atualizar.')
      print('='*30)
      sleep(1.5)
    else: # Se houver agendamentos na fila
      print(f'Deve ser informado o CPF do indivíduo que deseja modificar o agendamento.')

      try: # Inicia um bloco para tratamento de erros na entrada do usuário
        # Pede ao usuário o ID do agendamento a ser modificado
        cpf_agendamento = int(input("Digite o CPF: "))
        print('-'*30)

        agendamento_encontrado = None # Variável para armazenar o agendamento se ele for encontrado

        for agendamento in Agendamento.fila:
          if agendamento.cpf == cpf_agendamento:
            agendamento_encontrado = agendamento
            break

        if agendamento_encontrado: # Se o agendamento foi encontrado
          print(f'Preencha os **novos dados** para o agendamento {cpf_agendamento}.')

          # Coleta dos novos dados que substituirão os antigos
          novo_nome = str(input("Novo Nome: "))
          novo_cpf = int(input("Novo CPF (apenas números): "))
          novo_c_sus = int(input("Novo Número do cartão do SUS (apenas números): "))
          novo_c_residencia = int(input("Novo Número da residência (apenas números): "))
          novo_telefone = int(input("Número de telefone (apenas números): "))
          dia_random = random.randint(1 ,28) # Gera um dia aleatório para a data do agendamento
          mes_random = random.randint(1 ,12) # Gera um mês aleatório para a data do agendamento
          ano_random = random.randint(2025, 2030) # Gera um ano aleatório para a data do agendamento
          novo_data_agendamento = (f"{dia_random}/{mes_random}/{ano_random}") # Formata a data de agendamento

          while True:
            print("--------- Tipos de Agendamentos ---------")
            print("1. Cardiologista")
            print("2. Ortopedista")
            print("3. Pediatra")
            print("4. Oftalmologista")
            print("5. Neurologista")
            print("6. Clínico Geral")

            try:
              tipo = int(input("Escolha qual o tipo de agendamento.").strip()) # Solicita o tipo de agendamento e converte para inteiro
            except ValueError: # Captura o erro se o usuário não digitar um número
              print("Não temos esse tipo de agendamento. Digite um número.")
              sleep(1)
              continue

            if tipo == 1:
              novo_tipo = "Cardiologista" # Define o novo tipo de agendamento como Cardiologista
              break
            elif tipo == 2:
              novo_tipo = "Ortopedista" # Define o novo tipo de agendamento como Ortopedista
              break
            elif tipo == 3:
              novo_tipo = "Pediatra" # Define o novo tipo de agendamento como Pediatra
              break
            elif tipo == 4:
              novo_tipo = "Oftalmologista" # Define o novo tipo de agendamento como Oftalmologista
              break
            elif tipo == 5:
              novo_tipo = "Neurologista" # Define o novo tipo de agendamento como Neurologista
              break
            elif tipo == 6:
              novo_tipo = "Clínico Geral" # Define o novo tipo de agendamento como Clínico Geral
              break
            else:
              print("Tipo inválido, tente novamente.") # Mensagem para tipo inválido se a opção não for de 1 a 6
          novo_tipo_agendamento = novo_tipo # Atribui o novo tipo de agendamento selecionado

          # Chama o método de classe 'atualizar' para realizar a modificação no objeto
          Agendamento.atualizar(cpf_agendamento, novo_nome, novo_cpf, novo_c_sus, novo_c_residencia, novo_telefone, novo_data_agendamento, novo_tipo_agendamento)
        else: # Se o agendamento não foi encontrado após o loop
          sleep(1.5)
          print('='*30)
          print(f'Não foi encontrado nenhum agendamento com esse CPF {cpf_agendamento} para atualizar.')
          print('='*30)
          sleep(1.5)

      except ValueError: # Captura o erro se o usuário digitar texto onde é esperado um número (ID, CPF, SUS, Residência)
        # Tratamento de erro caso o usuário digite texto onde é esperado um número (ID, CPF, SUS, Residência)
        print("Entrada inválida. O ID, CPF, SUS, Residência ou Telefone2 devem ser válidos. Tente novamente.") # Informa sobre a entrada inválida
        sleep(1.5)


  elif opcao == 0:
    print("Encerrando o sistema. Até logo")
    break

  else: # Se a opção for inválida (fora das opções 0-5)
    print("Opção inválida, tente novamente.")