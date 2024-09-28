# depositar.py:
from utils import pausar_execucao

def depositar(saldo, extrato):
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
    return saldo, extrato


