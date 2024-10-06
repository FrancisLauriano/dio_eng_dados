
from utils import pausar_execucao

def listar_contas(contas):
    if contas:
        for conta in contas:
            usuario = conta['usuario']
            print(f'Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {usuario['nome']} (CPF: {usuario['cpf']})')
    else:
        print('Nenhuma conta cadastrada.')
    pausar_execucao()    
   
