from abc import ABC, abstractmethod

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor    

    def registrar(self, conta):
        if conta.depositar(self._valor):
            print(f'Depósito de R$ {self.valor:.2f} realizado com sucesso.')

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor       

    def registrar(self, conta):
        if conta.sacar(self._valor):
            print(f'Saque de R$ {self.valor:.2f} realizado com sucesso.')
