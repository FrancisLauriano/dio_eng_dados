from utils import pausar_execucao

def exibir_extrato(saldo, extrato):
    print(f'\n' + ' EXTRATO '.center(30, '#'))
    if not extrato:
        print(f'Não foram realizadas movimentações.')
    else:
        for item in extrato:
            print(item)
        print(f'Saldo atual: R$ {saldo:.2f}')
    print(f'#' * 30)
    pausar_execucao()


    