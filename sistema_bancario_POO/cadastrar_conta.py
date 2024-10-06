from utils import pausar_execucao

def cadastrar_conta(usuarios, contas):
    cpf = input('Informe o CPF do usuário para vincular à conta: ')
    
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    
    if usuario:
        numero_conta = len(contas) + 1
        
        conta = {
            'agencia': '0001',
            'numero_conta': numero_conta,
            'usuario': usuario,
            'saldo': 0,
            'extrato': [],
            'limite_saque': 500,
            'numero_saques': 0,
            'limite_saques': 3
        }
        contas.append(conta)
        print(f'Conta criada com sucesso! Agência: 0001 | Número da Conta: {numero_conta}')
    else:
        print('Usuário não encontrado. Verifique o CPF informado.')
    
    pausar_execucao()
  
   
