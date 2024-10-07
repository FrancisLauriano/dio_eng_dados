from datetime import datetime

class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, descricao, saldo_atual):
        """Adiciona uma transação ao histórico, incluindo o saldo da conta no momento."""
        self._transacoes.append({
            "descricao": descricao,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "saldo": saldo_atual
        })

    def exibir(self):
        """Exibe todas as transações do histórico com data, descrição e saldo."""
        if not self._transacoes:
            print('Nenhuma transação realizada.')
        else:
            print(f'\n' + ' EXTRATO '.center(50, '#'))
            for transacao in self._transacoes:
                print(f"{transacao['data']}: {transacao['descricao']}")
            print('-'*50)    
            print(f"{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} Saldo Total: R$ {transacao['saldo']:.2f}")    


