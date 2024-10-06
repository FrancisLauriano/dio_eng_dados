from utils import pausar_execucao

def exibir_extrato(contas, /):
    agencia = input('Informe a agência: ')
    numero_conta = input('Informe o número da conta: ')

    conta = next((conta for conta in contas if conta['agencia'] == agencia and str(conta['numero_conta']) == numero_conta), None)
    
    if not conta:
        print('Conta não encontrada. Verifique os dados e tente novamente.')
        pausar_execucao()
        return
    
    print(f'\n' + f' EXTRATO da conta {conta['numero_conta']} (Agência: {conta['agencia']}) '.center(50,'#'))
    if not conta['extrato']:
        print('Não foram realizadas movimentações.')
    else:
        for item in conta['extrato']:
            print(item)
        print(f'Saldo atual: R$ {conta['saldo']:.2f}')
    print('#' * 50)
    
    pausar_execucao()




    