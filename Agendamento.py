from collections import deque
from time import sleep

class Agendamento:
    fila = deque()
    proximo_id = 1

    def __init__(self, nome, cpf, c_sus, c_residencia):
        self.cpf = cpf
        self.agendamento_id = Agendamento.proximo_id
        self.nome = nome
        self.c_sus = c_sus
        self.c_residencia = c_residencia
        Agendamento.proximo_id += 1

    def __str__(self):
        return f"Agendamento {self.agendamento_id} (Nome: {self.nome}, CPF: {self.cpf}, C_SUS: {self.c_sus}, C_Residencia: {self.c_residencia})"

    @classmethod
    def add(cls, nome, cpf, c_sus, c_residencia):
        novo_agendamento = cls(nome, cpf, c_sus, c_residencia)
        cls.fila.append(novo_agendamento)
        sleep(1.5)
        print(f'{novo_agendamento.nome} foi agendado com sucesso!')
        sleep(1.5)

    @classmethod
    def mostrar_fila(cls):
        if cls.fila:
            for fila_agendamento in cls.fila:
                print(fila_agendamento)
        else:
            print('Nenhuma fila de agendamento')


    @classmethod
    def checar_agendamento(cls, numero_agendamento):
        if not cls.fila:
            print(f'Não há agendamentos marcados.')
            print('='*30)
            sleep(1.5)
            return
        elif cls.fila:
            for fila_agendamento in cls.fila:
                if not fila_agendamento.agendamento_id == numero_agendamento:
                    print(f'Não foi encontrado nenhum agendamento com o ID indicado.')
                    print('='*30)
                    sleep(1.5)
                    return
        else:
            for fila_agendamento in cls.fila:
                if fila_agendamento.agendamento_id == numero_agendamento:
                    print(fila_agendamento)
                    print('='*30)
                    sleep(1.5)
                    return

#p1 = Agendamento.add("Fernando da Silva", 1111111, 1111111, 1111111)

while True:
    print("--------- Menu Principal ---------")
    print("1. Fazer agendamento")
    print("2. Checar agendamento")
    print("3. Mostrar fila de clientes")
    print("0. Sair do sistema")

    opcao = int(input("Escolha a opção: ").strip())

    if opcao == 1:
        print('-'*30)
        print(f'Area de agendamento. Preencha os dados a seguir.')
        nomeInput = str(input("Nome: "))
        cpfInput = int(input("CPF (apenas números): "))
        c_susInput = int(input("Número do cartão do SUS (apenas números): "))
        c_residenciaInput = int(input("Número do cartão de residencia (apenas números): "))
        print('-'*30)
        Agendamento.add(nomeInput, cpfInput, c_susInput, c_residenciaInput)

    elif opcao == 2:
        print('='*30)
        sleep(1)
        print(f'Qual o ID de agendamento que deseja buscar?')
        numero_agendamento = int(input("ID do agendamento: "))
        print('='*30)
        sleep(1.5)
        Agendamento.checar_agendamento(numero_agendamento)

    elif opcao == 3:
        print('-'*30)
        sleep(1.5)
        Agendamento.mostrar_fila()
        sleep(1.5)

    elif opcao == 0:
        print("Encerrando o sistema. Até logo")
        break

    else:
        print("Opção invalida tente novamente.")