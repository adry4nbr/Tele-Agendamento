#Função de Reagedamento adicionado
from collections import deque # Importa a classe deque para gerenciar a fila de agendamentos
from time import sleep # Importa a função sleep para pausar a execução do programa
import random # Importa a biblioteca random para gerar números aleatórios

class Agendamento:
  fila = deque() # Fila estática (da classe) para armazenar todos os agendamentos
  fila_reagendamento = deque() # Fila para armazenar agendamentos que precisam ser reagendados
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

  # METODO DE ADICIONAR
  @classmethod # Decorador para definir um método de classe
  def add(cls, nome, cpf, c_sus, c_residencia, telefone, data_agendamento, tipo_agendamento): # Método de classe para adicionar um novo agendamento à fila (CREATE)
    novo_agendamento = cls(nome, cpf, c_sus, c_residencia, telefone, data_agendamento, tipo_agendamento) # Cria uma nova instância de Agendamento
    cls.fila.append(novo_agendamento) # Adiciona o novo agendamento ao final da fila
    sleep(1.5) # Pausa por 1.5 segundos
    print(f'{novo_agendamento.nome} foi agendado com sucesso!') # Informa que o agendamento foi adicionado
    sleep(1.5) # Pausa por 1.5 segundos
    return

  @classmethod
  def checar_agendamento(cls, cpf_to_check): # Método de classe para verificar um agendamento pelo CPF (READ específico)
    for agendamento in cls.fila: # Itera sobre cada agendamento na fila
      if agendamento.cpf == cpf_to_check: # Se o CPF do agendamento corresponder
        print(agendamento) # Imprime os detalhes do agendamento encontrado
        print(f"{agendamento.nome} está agendado.") # Informa que o agendamento foi encontrado
        print('='*30)
        sleep(1.5)
        return agendamento # Retorna o objeto agendamento encontrado

    # Se chegarmos aqui, o CPF não foi encontrado após verificar todos os agendamentos
    print(f'Não foi encontrado nenhum agendamento para o CPF {cpf_to_check}.') # Informa que o agendamento não foi encontrado
    print('='*30)
    sleep(1.5)
    return None

  # METODO DE ATUALIZAR
  @classmethod
  def atualizar(cls, cpf_to_update, novo_nome, novo_cpf, novo_c_sus, novo_c_residencia, novo_telefone, novo_data_agendamento, novo_tipo_agendamento): # Método para atualizar um agendamento (UPDATE)
    for agendamento in cls.fila: # Itera sobre cada agendamento na fila
      if agendamento.cpf == cpf_to_update: # Se o CPF do agendamento corresponder

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
        print(f"Agendamento de CPF: {cpf_to_update} de {nome_antigo} atualizado para:") # Informa que o agendamento foi atualizado
        print(agendamento) # Imprime os detalhes do agendamento atualizado
        print('='*30)
        sleep(1.5)
        return agendamento # Retorna o agendamento atualizado

    # Se chegar aqui, o CPF não foi encontrado
    sleep(1.5)
    print('='*30)
    print(f'Não foi encontrado nenhum agendamento com o CPF {cpf_to_update} para atualizar.') # Informa que o agendamento não foi encontrado
    print('='*30)
    sleep(1.5)
    return None


  # METODO DE REMOVER
  @classmethod # Decorador para definir um método de classe
  def remover(cls, cpf_to_remove): # Método de classe para remover um agendamento pelo CPF (DELETE)
    if not cls.fila: # Verifica se a fila está vazia
      print('Não há agendamentos para remover.') # Informa que não há agendamentos para remover
      print('='*30)
      sleep(1.5)
      return None

    found = False # Flag para indicar se o agendamento foi encontrado
    nova_fila = deque() # Cria uma nova fila vazia
    agendamento_removido = None # Variável para armazenar o agendamento removido

    for agendamento in cls.fila: # Itera sobre os agendamentos na fila atual
      if agendamento.cpf == cpf_to_remove and not found: # Se o CPF corresponder e ainda não foi encontrado
        agendamento_removido = agendamento # Armazena o agendamento a ser removido
        cls.fila_reagendamento.append(agendamento_removido) # Adiciona o agendamento removido à fila de reagendamento
        found = True # Marca como encontrado para não remover outros com o mesmo CPF
      else: # Se não for o agendamento a ser removido ou já foi encontrado
        nova_fila.append(agendamento) # Adiciona o agendamento à nova fila

    if found: # Se o agendamento foi encontrado e removido
      cls.fila = nova_fila # Substitui a fila antiga pela nova (sem o agendamento removido)
      print(f'Agendamento {agendamento_removido.agendamento_id} de {agendamento_removido.nome} (CPF: {agendamento_removido.cpf}) removido com sucesso e movido para a fila de reagendamento!') # Informa sobre a remoção e movimento para fila de reagendamento
      print('='*30)
      sleep(1.5)
      return agendamento_removido
    else: # Se o agendamento não foi encontrado
      print(f'Não foi encontrado nenhum agendamento com o CPF {cpf_to_remove} para remover.') # Informa que o agendamento não foi encontrado
      print('='*30)
      sleep(1.5)
      return None

  # METODO DE REAGENDAMENTO
  @classmethod
  def reagendamento(cls, cpf_to_reagendar):
    if not cls.fila_reagendamento: # Verifica se a fila de reagendamento está vazia
        print("Não há agendamentos na fila de reagendamento.") # Informa que não há agendamentos para reagendar
        sleep(1.5)
        return None

    agendamento_encontrado = None # Inicializa a variável para o agendamento encontrado
    for agendamento in cls.fila_reagendamento: # Itera sobre os agendamentos na fila de reagendamento
        if agendamento.cpf == cpf_to_reagendar: # Se o CPF do agendamento corresponder
            agendamento_encontrado = agendamento # Atribui o agendamento encontrado
            break

    if agendamento_encontrado: # Se o agendamento foi encontrado na fila de reagendamento
        print(f"Reagendando agendamento para {agendamento_encontrado.nome} (CPF: {agendamento_encontrado.cpf}).") # Informa qual agendamento está sendo reagendado

        while True:
          dia_random = random.randint(1 ,28) # Gera um dia aleatório para a data do agendamento
          mes_random = random.randint(1 ,12) # Gera um mês aleatório para a data do agendamento
          ano_random = random.randint(2025, 2030) # Gera um ano aleatório para a data do agendamento
          nova_data = (f"{dia_random}/{mes_random}/{ano_random}") # Formata a nova data de agendamento
          print(f"Nova Data de Agendamento : {nova_data}") # Exibe a nova data sugerida
          agendamento_encontrado.data_agendamento = nova_data # Assign the new date
          break

        while True:
            print("--------- Tipos de Agendamentos ---------") # Exibe as opções de tipo de agendamento
            print("1. Cardiologista")
            print("2. Ortopedista")
            print("3. Pediatra")
            print("4. Oftalmologista")
            print("5. Neurologista")
            print("6. Clínico Geral")
            try:
                tipo_input = int(input("Escolha qual o novo tipo de agendamento: ").strip()) # Solicita o novo tipo de agendamento
                if tipo_input == 1:
                    agendamento_encontrado.tipo_agendamento = "Cardiologista"
                    break
                elif tipo_input == 2:
                    agendamento_encontrado.tipo_agendamento = "Ortopedista"
                    break
                elif tipo_input == 3:
                    agendamento_encontrado.tipo_agendamento = "Pediatra"
                    break
                elif tipo_input == 4:
                    agendamento_encontrado.tipo_agendamento = "Oftalmologista"
                    break
                elif tipo_input == 5:
                    agendamento_encontrado.tipo_agendamento = "Neurologista"
                    break
                elif tipo_input == 6:
                    agendamento_encontrado.tipo_agendamento = "Clínico Geral"
                    break
                else:
                    print("Tipo inválido, tente novamente.") # Mensagem para tipo inválido
            except ValueError:
                print("Não temos esse tipo de agendamento. Digite um número.") # Mensagem para entrada inválida
                sleep(1)

        cls.fila_reagendamento.remove(agendamento_encontrado) # Remove o agendamento da fila de reagendamento
        cls.fila.append(agendamento_encontrado) # Adiciona o agendamento de volta à fila principal

        sleep(1.5)
        print('='*30)
        print(f"Agendamento para {agendamento_encontrado.nome} (CPF: {agendamento_encontrado.cpf}) reagendado com sucesso!") # Informa sobre o reagendamento bem-sucedido
        print(agendamento_encontrado)
        print('='*30)
        sleep(1.5)
        return agendamento_encontrado
    else:
        print(f"Agendamento com CPF {cpf_to_reagendar} não encontrado na fila de reagendamento.") # Informa que o agendamento não foi encontrado
        sleep(1.5)
        return None


# Pra ficar algumas pessoas aleatórias adicionadas no sistema (inicialização) ===============================
p1 = Agendamento.add("Fernando da Silva", 1, 1111111, 1111111, 1111111, "31/12/2026", "Cardiologista") # Adiciona um agendamento inicial
p2 = Agendamento.add("Alicia Costa", 2, 2222222, 2222222, 2222222, "30/09/26", "Neurologista") # Adiciona outro agendamento inicial
p3 = Agendamento.add("Felicia de Melo", 3, 33333333, 33333333, 33333333, "10/02/27", "Pediatra") # Adiciona um terceiro agendamento inicial
#=============================================================================================================z

while True: # Loop principal do menu do programa
  print("--------- Menu Principal ---------") # Exibe o cabeçalho do menu
  print("1. Fazer agendamento") # Opção para criar um agendamento
  print("2. Checar agendamento") # Opção para verificar um agendamento
  print("3. Remover agendamento") # Opção para remover um agendamento
  print("4. Atualizar agendamento") # Opção para atualizar um agendamento
  print("5. Fazer Reagendamento") # Opção para reagendar um agendamento
  print("0. Sair do sistema") # Opção para sair do sistema

  try: # Inicia um bloco para tratamento de erros
    opcao = int(input("Escolha a opção: ").strip()) # Solicita a opção do usuário e remove espaços em branco
  except ValueError: # Captura o erro se o usuário não digitar um número
    print("Opção inválida. Por favor, digite um número.") # Mensagem de erro para entrada inválida
    sleep(1)
    continue # Continua para a próxima iteração do loop

  if opcao == 1:
    print('-'*30)
    print(f'Area de agendamento. Preencha os dados a seguir.') # Solicita os dados do agendamento
    try:
      nomeInput = str(input("Nome: ")) # Solicita o nome
      cpfInput = int(input("CPF (apenas números): ")) # Solicita o CPF
      c_susInput = int(input("Número do cartão do SUS (apenas números): ")) # Solicita o cartão SUS
      c_residenciaInput = int(input("Número da residência (apenas números): ")) # Solicita o cartão de residência
      telefoneInput = int(input("Número de telefone (apenas números): ")) # Solicita o telefone
      dia_random = random.randint(1 ,28) # Gera um dia aleatório para a data do agendamento
      mes_random = random.randint(1 ,12) # Gera um mês aleatório para a data do agendamento
      ano_random = random.randint(2025, 2030) # Gera um ano aleatório para a data do agendamento
      data_agendamento = (f"{dia_random}/{mes_random}/{ano_random}") # Formata a data de agendamento
      print(f"Essa é a data do agendamento: {data_agendamento}") # Exibe a data gerada
      while True:
        print("--------- Tipos de Agendamentos ---------") # Exibe os tipos de agendamento disponíveis
        print("1. Cardiologista")
        print("2. Ortopedista")
        print("3. Pediatra")
        print("4. Oftalmologista")
        print("5. Neurologista")
        print("6. Clínico Geral")

        try:
          tipo = int(input("Escolha qual o tipo de agendamento.").strip()) # Solicita o tipo de agendamento
        except ValueError: # Captura o erro se o usuário não digitar um número
          print("Não temos esse tipo de agendamento. Digite um número.") # Mensagem de erro
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
          print("Tipo inválido, tente novamente.") # Mensagem para tipo inválido
      tipo_agendamentoInput = tipo # Atribui o tipo de agendamento selecionado
      print('-'*30)
      Agendamento.add(nomeInput, cpfInput, c_susInput, c_residenciaInput, telefoneInput, data_agendamento, tipo_agendamentoInput) # Chama o método para adicionar o agendamento
    except ValueError:
      print("Entrada inválida para CPF, SUS, Residência ou Telefone. Por favor, digite apenas números.") # Mensagem de erro para entrada inválida
      sleep(1.5)

  elif opcao == 2: # Se a opção for 2 (Checar agendamento)
    print('='*30)
    sleep(1)
    if not Agendamento.fila: # Verifica se a fila está vazia
      print(f'Não há agendamentos marcados.') # Mensagem se a fila estiver vazia
      print('='*30)
      sleep(1.5)
    else: # Se a fila não estiver vazia
      print(f'Para checar um agendamento é preciso o CPF do indivíduo.') # Solicita o CPF
      try: # Adiciona tratamento de erro para a entrada do ID
        cpf_agendamento = int(input("Digite o CPF: ")) # Solicita o CPF
        print('='*30)
        sleep(1.5)
        Agendamento.checar_agendamento(cpf_agendamento) # Chama o método para checar o agendamento
      except ValueError: # Captura o erro se o usuário não digitar um número
        print("Entrada inválida. O CPF deve ser apenas números. Tente novamente.") # Mensagem de erro
        sleep(1.5)

  elif opcao == 3: # Se a opção for 3 (Remover agendamento)
    print('='*30)
    sleep(1)
    if not Agendamento.fila: # Verifica se a fila está vazia
      print('Não há agendamentos para remover.') # Mensagem se a fila estiver vazia
      print('='*30)
      sleep(1.5)
    else: # Se a fila não estiver vazia
      print(f'É necessário informar o CPF do indivíduo que deseja remover o agendamento.') # Solicita o CPF
      try: # Adiciona tratamento de erro para a entrada do ID
          cpf_agendamento = int(input("Digite o CPF: ")) # Solicita o CPF
          print('='*30)
          sleep(1.5)
          Agendamento.remover(cpf_agendamento) # Chama o método para remover o agendamento
      except ValueError: # Captura o erro se o usuário não digitar um número
          print("Entrada inválida. O CPF deve ser apenas números. Tente novamente.") # Mensagem de erro
          sleep(1.5)

  elif opcao == 4: # Se a opção for 4 (Atualizar agendamento - UPDATE)
    print('='*30)
    sleep(1)

    # Verifica se a fila de agendamentos está vazia antes de tentar atualizar
    if not Agendamento.fila: # Se a fila estiver vazia
      print(f'Não há agendamentos para atualizar.') # Mensagem se a fila estiver vazia
      print('='*30)
      sleep(1.5)
    else: # Se houver agendamentos na fila
      print(f'Deve ser informado o CPF do indivíduo que deseja modificar o agendamento.') # Solicita o CPF para modificação

      try: # Inicia um bloco para tratamento de erros na entrada do usuário
        # Pede ao usuário o ID do agendamento a ser modificado
        cpf_agendamento = int(input("Digite o CPF: ")) # Solicita o CPF
        print('-'*30)

        agendamento_encontrado = None # Variável para armazenar o agendamento se ele for encontrado

        for agendamento in Agendamento.fila:
          if agendamento.cpf == cpf_agendamento:
            agendamento_encontrado = agendamento
            break

        if agendamento_encontrado: # Se o agendamento foi encontrado
          print(f'Preencha os **novos dados** para o agendamento de nome {agendamento_encontrado.nome} com o CPF: {cpf_agendamento}.') # Solicita os novos dados

          # Coleta dos novos dados que substituirão os antigos
          novo_nome = str(input("Novo Nome: ")) # Solicita novo nome
          novo_cpf = int(input("Novo CPF (apenas números): ")) # Solicita novo CPF
          novo_c_sus = int(input("Novo Número do cartão do SUS (apenas números): ")) # Solicita novo cartão SUS
          novo_c_residencia = int(input("Novo Número da residência (apenas números): ")) # Solicita novo cartão de residência
          novo_telefone = int(input("Número de telefone (apenas números): ")) # Solicita novo telefone
          dia_random = random.randint(1 ,28) # Gera um dia aleatório para a nova data
          mes_random = random.randint(1 ,12) # Gera um mês aleatório para a nova data
          ano_random = random.randint(2025, 2030) # Gera um ano aleatório para a nova data
          novo_data_agendamento = (f"{dia_random}/{mes_random}/{ano_random}") # Formata a nova data de agendamento

          while True:
            print("--------- Tipos de Agendamentos ---------") # Exibe os tipos de agendamento disponíveis
            print("1. Cardiologista")
            print("2. Ortopedista")
            print("3. Pediatra")
            print("4. Oftalmologista")
            print("5. Neurologista")
            print("6. Clínico Geral")

            try:
              tipo = int(input("Escolha qual o tipo de agendamento.").strip()) # Solicita o novo tipo de agendamento
            except ValueError: # Captura o erro se o usuário não digitar um número
              print("Não temos esse tipo de agendamento. Digite um número.") # Mensagem de erro
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
              print("Tipo inválido, tente novamente.") # Mensagem para tipo inválido
          novo_tipo_agendamento = novo_tipo # Atribui o novo tipo de agendamento selecionado

          # Chama o método de classe 'atualizar' para realizar a modificação no objeto
          Agendamento.atualizar(cpf_agendamento, novo_nome, novo_cpf, novo_c_sus, novo_c_residencia, novo_telefone, novo_data_agendamento, novo_tipo_agendamento)
        else: # Se o agendamento não foi encontrado após o loop
          sleep(1.5)
          print('='*30)
          print(f'Não foi encontrado nenhum agendamento com esse CPF {cpf_agendamento} para atualizar.') # Mensagem se o agendamento não foi encontrado
          print('='*30)
          sleep(1.5)

      except ValueError: # Captura o erro se o usuário digitar texto onde é esperado um número (ID, CPF, SUS, Residência)
        # Tratamento de erro caso o usuário digite texto onde é esperado um número (ID, CPF, SUS, Residência)
        print("Entrada inválida. O ID, CPF, SUS, Residência ou Telefone devem ser válidos. Tente novamente.") # Informa sobre a entrada inválida
        sleep(1.5)

  elif opcao == 5:
    print('='*30)
    sleep(1)

    if not Agendamento.fila_reagendamento: # Se a fila de reagendamento estiver vazia
      print(f'Não há agendamentos para reagendar.') # Mensagem se a fila de reagendamento estiver vazia
      print('='*30)
      sleep(1.5)
    else:
      print(f'Deve ser informado o CPF do indivíduo que deseja fazer o reagendamento.') # Solicita o CPF para reagendamento

      try: # Inicia um bloco para tratamento de erros na entrada do usuário
        cpf_reagendamento = int(input("Digite o CPF do agendamento para reagendar: ")) # Solicita o CPF para reagendar
        print('-'*30)
        Agendamento.reagendamento(cpf_reagendamento) # Chama o método de reagendamento

      except ValueError:
        print("Entrada de CPF inválida, tente novamente.") # Mensagem de erro para entrada inválida
        sleep(1.5)

  elif opcao == 0:
    print("Encerrando o sistema. Até logo") # Mensagem de encerramento
    break # Sai do loop principal

  else: # Se a opção for inválida (fora das opções 0-5)
    print("Opção inválida, tente novamente.") # Mensagem de erro para opção inválida