from time import sleep
from utils import limpar_terminal, pausar_execucao
from depositar import depositar
from sacar import sacar
from exibir_extrato import exibir_extrato


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
                saldo, extrato = depositar(saldo, extrato)
            elif opcao == 2:
                saldo, extrato, saques_realizados = sacar(saldo, extrato, saques_realizados, limite_saque, LIMITE_SAQUES_DIARIOS)
            elif opcao == 3:
                exibir_extrato(saldo, extrato)
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



