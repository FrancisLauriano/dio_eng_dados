from datetime import datetime
from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, limite=500, limite_saques=3):
        super().__init__(saldo, numero, agencia, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

    def saques_realizados_hoje(self):
        """Retorna o número de saques realizados hoje, usando o histórico."""
        hoje = datetime.now().strftime("%d/%m/%Y")
        saques_hoje = [
            transacao for transacao in self.historico._transacoes
            if "Saque" in transacao["descricao"] and transacao["data"].startswith(hoje)
        ]
        return len(saques_hoje)

    def sacar(self, valor):
        if valor <= 0:
            print('Valor inválido! O saque deve ser maior que zero.')
            return False

        if valor > self._limite:
            print(f'O limite máximo por saque é R$ {self._limite:.2f}.')
            return False

        if self.saques_realizados_hoje() >= self._limite_saques:
            print('Limite de saques diários atingido.')
            return False

        return super().sacar(valor)
