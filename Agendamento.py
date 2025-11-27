# metodo mostrar fila removido e atributo telefone, data de agendamento adicionado e o tipo de agendamento
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
      return # Sai da função após adicionar

  @classmethod # Decorador para definir um método de classe
  def checar_agendamento(cls, numero_agendamento): # Método de classe para verificar um agendamento pelo ID (READ específico)
      for fila_agendamento in cls.fila: # Itera sobre cada agendamento na fila
        if fila_agendamento.agendamento_id == numero_agendamento: # Se o ID do agendamento corresponder
            print(fila_agendamento) # Imprime os detalhes do agendamento encontrado
            print(f"{fila_agendamento.nome} está agendado") # Informa que o agendamento está marcado
            print('='*30) # Imprime uma linha separadora
            sleep(1.5) # Pausa por 1.5 segundos
            return # Sai da função após encontrar o agendamento
      # Se chegarmos aqui, o ID não foi encontrado após verificar todos os agendamentos
      print(f'Não foi encontrado nenhum agendamento com o ID indicado.') # Informa que o ID não foi encontrado
      print('='*30) # Imprime uma linha separadora
      sleep(1.5) # Pausa por 1.5 segundos

  @classmethod # Decorador para definir um método de classe
  def atualizar(cls, numero_agendamento, novo_nome, novo_cpf, novo_c_sus, novo_c_residencia, novo_telefone, novo_data_agendamento, novo_tipo_agendamento): # Método para atualizar um agendamento (UPDATE)
      for agendamento in cls.fila: # Itera sobre cada agendamento na fila
          if agendamento.agendamento_id == numero_agendamento: # Se o ID do agendamento corresponder

              nome_antigo = agendamento.nome # Armazena o nome antigo para exibição

              # Realiza a Atualização dos atributos
              agendamento.nome = novo_nome # Atualiza o nome
              agendamento.cpf = novo_cpf # Atualiza o CPF
              agendamento.c_sus = novo_c_sus # Atualiza o Cartão SUS
              agendamento.c_residencia = novo_c_residencia # Atualiza o Cartão de Residência
              agendamento.telefone = novo_telefone # Atualiza o telefone
              agendamento.data_agendamento = novo_data_agendamento # Atualiza a data do agendamento
              agendamento.tipo_agendamento = novo_tipo_agendamento # Atualiza o tipo de agendamento

              sleep(1.5) # Pausa por 1.5 segundos
              print('='*30) # Imprime uma linha separadora
              print(f"✅ Agendamento {numero_agendamento} de {nome_antigo} atualizado para:") # Confirma a atualização
              print(agendamento) # Imprime os detalhes do agendamento atualizado
              print('='*30) # Imprime uma linha separadora
              sleep(1.5) # Pausa por 1.5 segundos
              return # Sai da função após a atualização

      # Se chegar aqui, o ID não foi encontrado
      sleep(1.5) # Pausa por 1.5 segundos
      print('='*30) # Imprime uma linha separadora
      print(f'Não foi encontrado nenhum agendamento com o ID {numero_agendamento} para atualizar.') # Informa que o agendamento não foi encontrado para atualização
      print('='*30) # Imprime uma linha separadora
      sleep(1.5) # Pausa por 1.5 segundos

  @classmethod # Decorador para definir um método de classe
  def remover(cls, numero_agendamento): # Método de classe para remover um agendamento pelo ID (DELETE)
      if not cls.fila: # Verifica se a fila está vazia
          print('Não há agendamentos para remover.') # Informa que não há agendamentos
          print('='*30) # Imprime uma linha separadora
          sleep(1.5) # Pausa por 1.5 segundos
          return # Sai da função

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
          print(f'Agendamento {agendamento_removido.agendamento_id} de {agendamento_removido.nome} removido com sucesso!') # Confirma a remoção
          print('='*30) # Imprime uma linha separadora
          sleep(1.5) # Pausa por 1.5 segundos
      else: # Se o agendamento não foi encontrado
          print(f'Não foi encontrado nenhum agendamento com o ID {numero_agendamento} para remover.') # Informa que não foi encontrado
          print('='*30) # Imprime uma linha separadora
          sleep(1.5) # Pausa por 1.5 segundos

# Pra ficar algumas pessoas aleatórias adicionadas no sistema (inicialização)
p1 = Agendamento.add("Fernando da Silva", 1111111, 1111111, 1111111, 1111111, "31/12/2026", "Cardiologista") # Adiciona um agendamento inicial
p2 = Agendamento.add("Alicia Costa", 2222222, 2222222, 2222222, 2222222, "30/09/26", "Neurologista") # Adiciona outro agendamento inicial
p3 = Agendamento.add("Felicia de Melo", 33333333, 33333333, 33333333, 33333333, "10/02/27", "Pediatra") # Adiciona mais um agendamento inicial

while True: # Loop principal do menu do programa
  print("--------- Menu Principal ---------") # Título do menu
  print("1. Fazer agendamento") # Opção para fazer um novo agendamento (CREATE)
  print("2. Checar agendamento") # Opção para checar um agendamento existente (READ Específico)
  print("3. Remover agendamento") # Opção para remover um agendamento (DELETE)
  print("4. Atualizar agendamento") # Opção para atualizar um agendamento (UPDATE) <<< OPÇÃO ADICIONADA

  print("0. Sair do sistema") # Opção para sair do programa

  try: # Inicia um bloco para tratamento de erros
      opcao = int(input("Escolha a opção: ").strip()) # Solicita a opção ao usuário e converte para inteiro
  except ValueError: # Captura o erro se o usuário não digitar um número
      print("Opção inválida. Por favor, digite um número.") # Informa sobre a opção inválida
      sleep(1) # Pausa por 1 segundo
      continue # Continua para a próxima iteração do loop (mostra o menu novamente)

  if opcao == 1: # Se a opção for 1 (Fazer agendamento)
      print('-'*30) # Imprime uma linha separadora
      print(f'Area de agendamento. Preencha os dados a seguir.') # Informa para preencher os dados
      nomeInput = str(input("Nome: ")) # Pede o nome
      cpfInput = int(input("CPF (apenas números): ")) # Pede o CPF
      c_susInput = int(input("Número do cartão do SUS (apenas números): ")) # Pede o Cartão SUS
      c_residenciaInput = int(input("Número da residência (apenas números): ")) # Pede o Cartão de Residência
      telefoneInput = int(input("Número de telefone (apenas números): ")) # Pede o número de telefone
      dia_random = random.randint(1 ,28) # Gera um dia aleatório para a data do agendamento
      mes_random = random.randint(1 ,12) # Gera um mês aleatório para a data do agendamento
      ano_random = random.randint(2025, 2030) # Gera um ano aleatório para a data do agendamento
      data_agendamento = (f"{dia_random}/{mes_random}/{ano_random}") # Formata a data de agendamento
      while True:
        print("--------- Tipos de Agendamentos ---------") # Título para os tipos de agendamento
        print("1. Cardiologista") # Opção de Cardiologista
        print("2. Ortopedista") # Opção de Ortopedista
        print("3. Pediatra") # Opção de Pediatra
        print("4. Oftalmologista") # Opção de Oftalmologista
        print("5. Neurologista") # Opção de Neurologista
        print("6. Clínico Geral") # Opção de Clínico Geral

        try:
          tipo = int(input("Escolha qual o tipo de agendamento.").strip()) # Solicita o tipo de agendamento e converte para inteiro
        except ValueError: # Captura o erro se o usuário não digitar um número
          print("Não temos esse tipo de agendamento. Digite um número.") # Mensagem de erro para entrada inválida
          sleep(1) # Pausa por 1 segundo
          continue # Continua para a próxima iteração do loop

        if tipo == 1:
          tipo = "Cardiologista" # Define o tipo de agendamento como Cardiologista
          break # Sai do loop de escolha de tipo
        elif tipo == 2:
          tipo = "Ortopedista" # Define o tipo de agendamento como Ortopedista
          break # Sai do loop de escolha de tipo
        elif tipo == 3:
          tipo = "Pediatra" # Define o tipo de agendamento como Pediatra
          break # Sai do loop de escolha de tipo
        elif tipo == 4:
          tipo = "Oftalmologista" # Define o tipo de agendamento como Oftalmologista
          break # Sai do loop de escolha de tipo
        elif tipo == 5:
          tipo = "Neurologista" # Define o tipo de agendamento como Neurologista
          break # Sai do loop de escolha de tipo
        elif tipo == 6:
          tipo = "Clínico Geral" # Define o tipo de agendamento como Clínico Geral
          break # Sai do loop de escolha de tipo
        else:
          print("Tipo inválido, tente novamente.") # Mensagem para tipo inválido se a opção não for de 1 a 6
      tipo_agendamentoInput = tipo # Atribui o tipo de agendamento selecionado
      print('-'*30) # Imprime uma linha separadora
      Agendamento.add(nomeInput, cpfInput, c_susInput, c_residenciaInput, telefoneInput, data_agendamento, tipo_agendamentoInput) # Chama o método para adicionar o agendamento

  elif opcao == 2: # Se a opção for 2 (Checar agendamento)
      print('='*30) # Imprime uma linha separadora
      sleep(1) # Pausa por 1 segundo
      if not Agendamento.fila: # Verifica se a fila está vazia
        print(f'Não há agendamentos marcados.') # Informa que não há agendamentos
        print('='*30) # Imprime uma linha separadora
        sleep(1.5) # Pausa por 1.5 segundos
      else: # Se a fila não estiver vazia
        print(f'Qual o ID de agendamento que deseja buscar?') # Pede o ID do agendamento
        try: # Adiciona tratamento de erro para a entrada do ID
            numero_agendamento = int(input("ID do agendamento: ")) # Lê o ID e converte para inteiro
            print('='*30) # Imprime uma linha separadora
            sleep(1.5) # Pausa por 1.5 segundos
            Agendamento.checar_agendamento(numero_agendamento) # Chama o método para checar o agendamento
        except ValueError: # Captura o erro se o usuário não digitar um número
            print("Entrada inválida. O ID do agendamento deve ser um número. Tente novamente.") # Informa sobre a entrada inválida
            sleep(1.5) # Pausa por 1.5 segundos

  elif opcao == 3: # Se a opção for 3 (Remover agendamento)
      print('='*30) # Imprime uma linha separadora
      sleep(1) # Pausa por 1 segundo
      if not Agendamento.fila: # Verifica se a fila está vazia
          print(f'Não há agendamentos para remover.') # Informa que não há agendamentos para remover
          print('='*30) # Imprime uma linha separadora
          sleep(1.5) # Pausa por 1.5 segundos
      else: # Se a fila não estiver vazia
          print(f'Qual o ID do agendamento que deseja remover?') # Pede o ID do agendamento a remover
          try: # Adiciona tratamento de erro para a entrada do ID
              numero_agendamento = int(input("ID do agendamento a remover: ")) # Lê o ID e converte para inteiro
              print('='*30) # Imprime uma linha separadora
              sleep(1.5) # Pausa por 1.5 segundos
              Agendamento.remover(numero_agendamento) # Chama o método para remover o agendamento
          except ValueError: # Captura o erro se o usuário não digitar um número
              print("Entrada inválida. O ID do agendamento deve ser um número. Tente novamente.") # Informa sobre a entrada inválida
              sleep(1.5) # Pausa por 1.5 segundos

  elif opcao == 4: # Se a opção for 4 (Atualizar agendamento - UPDATE)
      print('='*30) # Imprime uma linha separadora
      sleep(1) # Pausa por 1 segundo

      # Verifica se a fila de agendamentos está vazia antes de tentar atualizar
      if not Agendamento.fila: # Se a fila estiver vazia
          print(f'Não há agendamentos para atualizar.') # Informa que não há agendamentos para atualizar
          print('='*30) # Imprime uma linha separadora
          sleep(1.5) # Pausa por 1.5 segundos
      else: # Se houver agendamentos na fila
          print(f'Qual o ID do agendamento que deseja atualizar?') # Pede o ID do agendamento a ser atualizado

          try: # Inicia um bloco para tratamento de erros na entrada do usuário
              # Pede ao usuário o ID do agendamento a ser modificado
              numero_agendamento = int(input("ID do agendamento a atualizar: ")) # Lê o ID e converte para inteiro
              print('-'*30) # Imprime uma linha separadora
              print(f'Preencha os **novos dados** para o agendamento {numero_agendamento}.') # Solicita os novos dados

              # Coleta dos novos dados que substituirão os antigos
              novo_nome = str(input("Novo Nome: ")) # Pede o novo nome
              novo_cpf = int(input("Novo CPF (apenas números): ")) # Pede o novo CPF
              novo_c_sus = int(input("Novo Número do cartão do SUS (apenas números): ")) # Pede o novo Cartão SUS
              novo_c_residencia = int(input("Novo Número da residência (apenas números): ")) # Pede o novo Cartão de Residência
              novo_telefone = int(input("Número de telefone (apenas números): ")) # Pede o novo número de telefone

              while True:
                print("--------- Tipos de Agendamentos ---------") # Título para os tipos de agendamento
                print("1. Cardiologista") # Opção de Cardiologista
                print("2. Ortopedista") # Opção de Ortopedista
                print("3. Pediatra") # Opção de Pediatra
                print("4. Oftalmologista") # Opção de Oftalmologista
                print("5. Neurologista") # Opção de Neurologista
                print("6. Clínico Geral") # Opção de Clínico Geral

                try:
                  tipo = int(input("Escolha qual o tipo de agendamento.").strip()) # Solicita o tipo de agendamento e converte para inteiro
                except ValueError: # Captura o erro se o usuário não digitar um número
                  print("Não temos esse tipo de agendamento. Digite um número.") # Mensagem de erro para entrada inválida
                  sleep(1) # Pausa por 1 segundo
                  continue # Continua para a próxima iteração do loop

                if tipo == 1:
                  novo_tipo = "Cardiologista" # Define o novo tipo de agendamento como Cardiologista
                  break # Sai do loop de escolha de tipo
                elif tipo == 2:
                  novo_tipo = "Ortopedista" # Define o novo tipo de agendamento como Ortopedista
                  break # Sai do loop de escolha de tipo
                elif tipo == 3:
                  novo_tipo = "Pediatra" # Define o novo tipo de agendamento como Pediatra
                  break # Sai do loop de escolha de tipo
                elif tipo == 4:
                  novo_tipo = "Oftalmologista" # Define o novo tipo de agendamento como Oftalmologista
                  break # Sai do loop de escolha de tipo
                elif tipo == 5:
                  novo_tipo = "Neurologista" # Define o novo tipo de agendamento como Neurologista
                  break # Sai do loop de escolha de tipo
                elif tipo == 6:
                  novo_tipo = "Clínico Geral" # Define o novo tipo de agendamento como Clínico Geral
                  break # Sai do loop de escolha de tipo
                else:
                  print("Tipo inválido, tente novamente.") # Mensagem para tipo inválido se a opção não for de 1 a 6
              novo_tipo_agendamento = novo_tipo # Atribui o novo tipo de agendamento selecionado

              # Chama o método de classe 'atualizar' para realizar a modificação no objeto
              # A data do agendamento é mantida a mesma que a original no update, ou uma nova lógica de data pode ser adicionada aqui.
              # No momento, 'data_agendamento' está sendo usado como a data original da adição, não uma nova data para atualização.
              Agendamento.atualizar(numero_agendamento, novo_nome, novo_cpf, novo_c_sus, novo_c_residencia, novo_telefone, data_agendamento, novo_tipo_agendamento)

          except ValueError: # Captura o erro se o usuário digitar texto onde é esperado um número (ID, CPF, SUS, Residência)
              # Tratamento de erro caso o usuário digite texto onde é esperado um número (ID, CPF, SUS, Residência)
              print("Entrada inválida. O ID, CPF, SUS e Residência devem ser números. Tente novamente.") # Informa sobre a entrada inválida
              sleep(1.5) # Pausa por 1.5 segundos


  elif opcao == 0: # Se a opção for 0 (Sair do sistema)
      print("Encerrando o sistema. Até logo") # Mensagem de encerramento
      break # Sai do loop principal, encerrando o programa

  else: # Se a opção for inválida (fora das opções 0-5)
      print("Opção inválida, tente novamente.") # Informa sobre a opção inválida