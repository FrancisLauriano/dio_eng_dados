from utils import pausar_execucao

def sacar(contas, /):
    agencia = input('Informe a agência: ')
    numero_conta = input('Informe o número da conta: ')

    conta = next((conta for conta in contas if conta['agencia'] == agencia and str(conta['numero_conta']) == numero_conta), None)
    
    if not conta:
        print('Conta não encontrada. Verifique os dados e tente novamente.')
        pausar_execucao()
        return
    
    titular = conta['usuario']
    
    print(f'\nConta encontrada: Agência {conta['agencia']}, Conta {conta['numero_conta']}')
    print(f'Titular: {titular['nome']} (CPF: {titular['cpf']})\n')
    
    confirmacao = input('Deseja continuar com o saque? (S/N): ').strip().upper()
    if confirmacao == 'S':
        try:
            valor_saque = float(input('Informe o valor do saque: R$ '))
            if conta['numero_saques'] >= conta['limite_saques']:
                print('Limite de saques diários atingido.')
            elif valor_saque > conta['saldo']:
                print('Saldo insuficiente!')
            elif valor_saque > conta['limite_saque']:
                print(f'O limite máximo por saque é R$ {conta['limite_saque']:.2f}.')
            elif valor_saque > 0:
                conta['saldo'] -= valor_saque
                conta['numero_saques'] += 1
                conta['extrato'].append(f'Saque: R$ {valor_saque:.2f}')
                print(f'Saque de R$ {valor_saque:.2f} realizado com sucesso!')
            else:
                print('O valor de saque deve ser positivo.')
        except ValueError:
            print('Valor inválido! Insira um número válido.')
    else:
        print('Operação cancelada.')
    
    pausar_execucao()




