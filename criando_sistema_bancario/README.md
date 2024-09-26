# Sistema Banário

Este é um projeto de Sistema Bancário Simples implementado em Python. Ele permite ao usuário realizar operações bancárias básicas como depositar, sacar e visualizar o extrato. A versão atual (V1) trabalha com apenas um único usuário, sem a necessidade de gerenciar contas e agências.


## Funcionalidades :video_game:

1. Depósito
   - O usuário pode depositar valores positivos na conta.
   - Todos os depósitos são registrados e podem ser visualizados no extrato.
  
2. Saque
   - O sistema permite até 3 saques diários, com um limite de R$ 500,00 por saque.
   - Se o saldo for insuficiente ou o número de saques diários for excedido, o sistema exibirá uma mensagem informando o erro.
   - Todos os saques realizados são registrados no extrato.
  
3. Extrato
   - O extrato lista todas as movimentações realizadas (depósitos e saques).
   - O saldo atual da conta é exibido ao final do extrato.
   - Se não houver movimentações, o sistema exibirá a mensagem "Não foram realizadas movimentações."


## Regras e Limitações :pencil:

- Depósitos: Apenas valores positivos são aceitos.
- Saques: O usuário pode realizar até 3 saques por dia, com o limite de R$ 500,00 por saque.
- Saldo: O sistema não permite saques que excedam o saldo disponível.


## Estrutura do Projeto :triangular_ruler: :straight_ruler:

- __main__.py: Arquivo principal que contém o menu de navegação e gerencia as operações bancárias.
- depositar.py: Contém a função que implementa a lógica para depósitos.
- sacar.py: Contém a função que implementa a lógica para saques.
- exibir_extrato.py: Função que exibe todas as movimentações (depósitos e saques) e o saldo final.
- utils.py: Funções auxiliares como limpar_terminal e pausar_execucao para melhorar a experiência do usuário.


## Tecnologias Utilizadas :hammer_and_wrench: :gear: :books:

- Python 3.x: Linguagem de programação utilizada para implementar o sistema.
- Módulo os: Usado para limpar o terminal entre as operações.
- Módulo time: Usado para pausar a execução e criar uma experiência de usuário mais interativa.


## Executar App :arrow_forward:

**development:**
```bash
python __main__.py
```




