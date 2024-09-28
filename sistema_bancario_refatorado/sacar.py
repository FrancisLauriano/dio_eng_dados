# sacar.py:
from utils import pausar_execucao

def sacar(saldo, extrato, saques_realizados, limite_saque, LIMITE_SAQUES_DIARIOS):
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
    return saldo, extrato, saques_realizados


