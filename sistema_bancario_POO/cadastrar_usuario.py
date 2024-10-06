from utils import pausar_execucao

def cadastrar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print('CPF já cadastrado. Não é possível cadastrar o mesmo CPF.')
        pausar_execucao()
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro – bairro – cidade / sigla do estado): ')

    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print('Usuário cadastrado com sucesso!')
    pausar_execucao()


