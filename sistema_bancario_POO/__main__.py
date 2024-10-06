from time import sleep
from utils import limpar_terminal, pausar_execucao
from depositar import depositar
from sacar import sacar
from exibir_extrato import exibir_extrato
from cadastrar_usuario import cadastrar_usuario
from cadastrar_conta import cadastrar_conta
from listar_contas import listar_contas

def sistema_bancario():
    usuarios = []
    contas = []

    while True:
        limpar_terminal()
        print(f'\n' + ' MENU '.center(30,'#'))
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
                depositar(contas)

            elif opcao == 2:
                sacar(contas)

            elif opcao == 3:
                exibir_extrato(contas)

            elif opcao == 4:
                cadastrar_usuario(usuarios)

            elif opcao == 5:
                cadastrar_conta(usuarios, contas)

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
                print('Opção Inválida. Tente novamente...')
                pausar_execucao()

        except ValueError:
            print('Opção inválida. Tente novamente.')
            pausar_execucao()

if __name__ == '__main__':
    sistema_bancario()





