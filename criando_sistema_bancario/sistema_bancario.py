from time import sleep
import os

def limpar_terminal():
    sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar_execucao():
    input('\nPressione ENTER para continuar... ')   


def sistema_bancario():
    saldo = 0
    limite_saque = 500
    extrato = []
    saques_realizados = 0
    LIMITE_SAQUES_DIARIOS = 3

    while True:
        limpar_terminal()
        print(f'\n' + ' MENU '.center(20,'#'))
        print(f'''[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair''')
        print(f'\n' + '#' * 20)

        try:
            opcao = int(input('OPÇÃO: '))
            limpar_terminal()

            if opcao == 1:
                try:
                    valor_deposito = float(input(f'Informe o valor do depósito: R$ '))
                    if valor_deposito > 0:
                        saldo += valor_deposito
                        extrato.append(f'Depósito: R$ {valor_deposito:.2f}')
                        print(f'Depósito de R$ {valor_deposito:.2f} realizado com sucesso!')
                    else:
                        print(f'Valor inválido! O depósito deve ser um valor positivo.')
                except ValueError:
                    print(f'Valor inválido! Insira um número válido.')
                pausar_execucao()

            elif opcao == 2:
                if saques_realizados >= LIMITE_SAQUES_DIARIOS:
                    print(f'Limite de saques diários atingido.')
                else:
                    try:
                        valor_saque = float(input(f'Informe o valor do saque: R$ '))
                        if valor_saque > saldo:
                            print(f'Saldo insuficiente!')
                        elif valor_saque > limite_saque:
                            print(f'O limite máximo por saque é R$ {limite_saque:.2f}.')
                        elif valor_saque > 0:
                            saldo -= valor_saque
                            saques_realizados += 1
                            extrato.append(f'Saque: R$ {valor_saque:.2f}')
                            print(f'Saque de R$ {valor_saque:.2f} realizado com sucesso!')
                        else:
                            print(f'O valor de saque deve ser positivo.')
                    except ValueError:
                        print(f'Valor inválido! Insira um número válido.')
                pausar_execucao()

            elif opcao == 3:
                print(f'\n' + ' EXTRATO '.center(30, '#'))
                if not extrato:
                    print(f'Não foram realizadas movimentações.')
                else:
                    for item in extrato:
                        print(item)
                    print(f'Saldo atual: R$ {saldo:.2f}')
                print(f'#' * 30)
                pausar_execucao()

            elif opcao == 0:
                limpar_terminal()
                print(f'Encerrando o sistema...')
                for i in range(5, 0, -1):
                    print('|' * i)
                    sleep(0.1)
                print(f'FINALIZADO')
                break

            else:
                print(f'Opção Inválida. Tente novamente...')
                pausar_execucao()

        except ValueError:
            print(f'Opção inválida. Tente novamente.')
            pausar_execucao()

if __name__ == '__main__':
    sistema_bancario()
