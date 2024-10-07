from pessoa_fisica import PessoaFisica
from conta_corrente import ContaCorrente
from transacoes import Deposito, Saque
from utils import limpar_terminal, pausar_execucao
from time import sleep

def sistema_bancario():
    clientes = []
    contas = []

    while True:
        limpar_terminal()
        print(f'\n' + ' MENU '.center(30, '#'))
        print('''[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Usuário
[5] Cadastrar Conta
[6] Listar Contas
[0] Sair''')
        print(f'\n' + '#' * 30)

        try:
            opcao = int(input('OPÇÃO: '))
            limpar_terminal()

            if opcao == 1:
                cpf = input('Informe o CPF do titular: ')
                conta = buscar_conta_por_cpf(cpf, contas)
                if conta:
                    valor = float(input('Valor do depósito: R$ '))
                    deposito = Deposito(valor)
                    deposito.registrar(conta)
                else:
                    print('\nConta não encontrada.')
                pausar_execucao()

            elif opcao == 2:
                cpf = input('Informe o CPF do titular: ')
                conta = buscar_conta_por_cpf(cpf, contas)
                if conta:
                    valor = float(input('Valor do saque: R$ '))
                    saque = Saque(valor)
                    saque.registrar(conta)
                else:
                    print('\nConta não encontrada.')
                pausar_execucao()

            elif opcao == 3:
                cpf = input('Informe o CPF do titular: ')
                conta = buscar_conta_por_cpf(cpf, contas)
                if conta:
                    conta.historico.exibir()
                else:
                    print('\nConta não encontrada.')
                pausar_execucao()

            elif opcao == 4:
                cadastrar_usuario(clientes)

            elif opcao == 5:
                cadastrar_conta(clientes, contas)

            elif opcao == 6:
                listar_contas(contas)

            elif opcao == 0:
                limpar_terminal()
                print(f'Encerrando o sistema...')
                for i in range(5, 0, -1):
                    print('|' * i)
                    sleep(0.1)
                print(f'FINALIZADO')
                break

            else:
                print('\nOpção Inválida. Tente novamente...')
                pausar_execucao()

        except ValueError:
            print('\nOpção inválida. Tente novamente.')
            pausar_execucao()

def buscar_conta_por_cpf(cpf, contas):
    for conta in contas:
        if conta._cliente.cpf == cpf:
            return conta
    return None

def cadastrar_usuario(clientes):
    cpf = input('Informe o CPF (somente números): ')
    if any(cliente.cpf == cpf for cliente in clientes):
        print('\nCPF já cadastrado. Não é possível cadastrar o mesmo CPF.')
        pausar_execucao()
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro – bairro – cidade / sigla do estado): ')

    cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
    clientes.append(cliente)
    print('\nUsuário cadastrado com sucesso!')
    pausar_execucao()

def cadastrar_conta(clientes, contas):
    cpf = input('Informe o CPF do titular: ')
    cliente = next((cliente for cliente in clientes if cliente.cpf == cpf), None)
    if cliente:
        numero_conta = len(contas) + 1
        conta = ContaCorrente(0, numero_conta, '0001', cliente, limite=500, limite_saques=3)
        cliente.adicionar_conta(conta)
        contas.append(conta)
        print(f'Conta criada com sucesso! Agência: 0001 | Número da Conta: {numero_conta}')
        pausar_execucao()
    else:
        print('Cliente não encontrado.')
        pausar_execucao()


def listar_contas(contas):
    if contas:
        for conta in contas:
            print(f'Agência: {conta._agencia} | Conta: {conta._numero} | Titular: {conta._cliente.nome} (CPF: {conta._cliente.cpf})')
    else:
        print('Nenhuma conta cadastrada.')
    pausar_execucao()

if __name__ == '__main__':
    sistema_bancario()
