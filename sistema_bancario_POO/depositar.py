from utils import pausar_execucao

def depositar(contas, /):
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
    
    confirmacao = input('Deseja continuar com o depósito? (S/N): ').strip().upper()
    if confirmacao == 'S':
        try:
            valor_deposito = float(input('Informe o valor do depósito: R$ '))
            if valor_deposito > 0:
                conta['saldo'] += valor_deposito
                conta['extrato'].append(f'Depósito: R$ {valor_deposito:.2f}')
                print(f'Depósito de R$ {valor_deposito:.2f} realizado com sucesso!')
            else:
                print('Valor inválido! O depósito deve ser um valor positivo.')
        except ValueError:
            print('Valor inválido! Insira um número válido.')
    else:
        print('Operação cancelada.')
    
    pausar_execucao()




