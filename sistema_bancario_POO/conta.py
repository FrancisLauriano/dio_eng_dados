from historico import Historico

class Conta:
    def __init__(self, saldo, numero, agencia, cliente):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print('Valor inválido! O saque deve ser maior que zero.')
            return False
        if valor > self._saldo:
            print('Saldo insuficiente!')
            return False
        self._saldo -= valor
        self._historico.adicionar_transacao(f"Saque de R$ {valor:.2f}", self._saldo)
        return True

    def depositar(self, valor):
        if valor <= 0:
            print('Valor inválido! O depósito deve ser maior que zero.')
            return False
        self._saldo += valor
        self._historico.adicionar_transacao(f"Depósito de R$ {valor:.2f}", self._saldo)
        return True
