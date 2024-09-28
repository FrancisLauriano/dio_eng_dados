# Sistema Bancário

Este é um projeto de Sistema Bancário Simples implementado em Python. Na versão atual (V2), o sistema permite que múltiplos usuários realizem operações bancárias básicas, como depositar, sacar e visualizar o extrato, além de permitir o cadastro de usuários e contas. Cada usuário pode ter mais de uma conta, e as operações são vinculadas a agências e números de contas específicos.


## Funcionalidades :video_game:

1. Depósito
   - O usuário pode depositar valores positivos em uma conta específica.
   - Para realizar um depósito, o usuário seleciona a agência e o número da conta.
   - Antes da operação, o sistema exibe as informações da conta (nome do titular e CPF) para confirmação.
   - Todos os depósitos são registrados e podem ser visualizados no extrato.
  
2. Saque
   - O sistema permite até 3 saques diários, com um limite de R$ 500,00 por saque.
   - O usuário deve selecionar a agência e o número da conta para realizar o saque.
   - O sistema exibe as informações da conta para confirmação antes de concluir a operação.
   - Se o saldo for insuficiente ou o número de saques diários for excedido, o sistema exibirá uma mensagem de erro.
   - Todos os saques realizados são registrados no extrato.
  
3. Extrato
   - O extrato lista todas as movimentações realizadas (depósitos e saques) para uma conta específica.
   - O saldo atual da conta é exibido ao final do extrato.
   - Se não houver movimentações, o sistema exibirá a mensagem "Não foram realizadas movimentações."

4. Cadastro de Usuários
   - Permite cadastrar novos usuários no sistema, inserindo nome, data de nascimento, CPF (apenas números) e endereço.
   - Não permite o cadastro de dois ou mais usuários com o mesmo CPF.

5. Cadastro de Contas
   - Permite vincular uma nova conta a um usuário existente, baseado no CPF.
   - O número da conta é gerado sequencialmente, e a agência é fixa em "0001".
   - Um usuário pode ter mais de uma conta, mas uma conta pertence a apenas um usuário.

6. Listar Contas
   - Lista todas as contas cadastradas, mostrando a agência, número da conta, nome do titular e CPF.


## Regras e Limitações :pencil:

- Depósitos: Apenas valores positivos são aceitos.
- Saques: O usuário pode realizar até 3 saques por dia, com um limite de R$ 500,00 por saque.
- Saldo: O sistema não permite saques que excedam o saldo disponível.
- Cadastro de Usuários: Não é possível cadastrar dois usuários com o mesmo CPF.
- Confirmação de Operações: Para cada operação de saque ou depósito, as informações da conta (nome do titular e CPF) são exibidas para confirmação antes de continuar.
- Múltiplas Contas: Um usuário pode ter mais de uma conta, mas cada conta pertence a somente um usuário.


## Estrutura do Projeto :triangular_ruler: :straight_ruler:

- __main__.py: Arquivo principal que contém o menu de navegação e gerencia as operações bancárias e cadastros.
- depositar.py: Contém a função que implementa a lógica para depósitos.
- sacar.py: Contém a função que implementa a lógica para saques.
- exibir_extrato.py: Função que exibe todas as movimentações (depósitos e saques) e o saldo final por conta.
- cadastrar_usuario.py: Função para cadastrar novos usuários.
- cadastrar_conta.py: Função para cadastrar contas vinculadas a usuários.
- listar_contas.py: Função para listar todas as contas cadastradas no sistema.
- utils.py: Funções auxiliares como limpar_terminal e pausar_execucao para melhorar a experiência do usuário.


## Tecnologias Utilizadas :hammer_and_wrench: :gear: :books:

- Python 3.12.3: Linguagem de programação utilizada para implementar o sistema.
- Módulo os: Usado para limpar o terminal entre as operações.
- Módulo time: Usado para pausar a execução e criar uma experiência de usuário mais interativa.


## Executar App :arrow_forward:

**development:**
```bash
python __main__.py
```




