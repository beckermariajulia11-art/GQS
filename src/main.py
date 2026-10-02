""" Sistema de Cadastro de Pessoas - versao 3"""

from cadastro import CadastroPessoas

def exibir_menu():
    """Exibe o menu principal e retorna a opcao escolhida."""
    print("=========================")
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Analisar pessoas")
    print("6 - Sair")
    return int(input("Escolha uma opcao: "))

def cadastrar_pessoa(cadastro):
    """Cadastra uma nova pessoa nas listas."""
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    email = input("Informe o email: ")

    cadastro.cadastrar(nome, idade, email)

    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def exibir_pessoa(pessoa):
    """Exibe os dados de uma pessoa."""
    print("Nome: " + pessoa.get_nome())
    print("Idade: " + str(pessoa.get_idade()))
    print("E-mail: " + pessoa.get_email())
    if pessoa.get_idade() >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def consultar_pessoa(cadastro):
    """Consulta uma pessoa pelo nome."""
    procurado = input("Nome para consultar: ")
    pessoa = cadastro.buscar_por_nome(procurado)

    if pessoa is None:
        print("Nao encontrado")
    else:
        exibir_pessoa(pessoa)

def alterar_pessoa(cadastro):
    """Altera os dados de uma pessoa existente."""
    procurado = input("Nome para alterar: ")
    pessoa = cadastro.buscar_por_nome(procurado)

    if pessoa is None:
        print("Nao encontrado")
    else:
        novo_nome = input("Novo nome: ")
        nova_idade = int(input("Nova idade: "))
        novo_email = input("Novo e-mail: ")
        cadastro.alterar(
            pessoa,
            novo_nome,
            nova_idade,
            novo_email
        )

        print("Pessoa alterada com sucesso!")
        exibir_pessoa(pessoa)

def listar_pessoas(cadastro):
    """Lista todas as pessoas cadastradas."""
    pessoas = cadastro.listar()

    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada")

    for pessoa in pessoas:
        exibir_pessoa(pessoa)
        print("------------------------")

    print("Total: " + str(len(pessoas)))

def analisar_faixa_etaria(idade):
    """Analisa a faixa etaria de uma pessoa."""
    if idade < 12:
        print("Faixa etaria: Crianca")
    elif idade < 18:
        print("Faixa etaria: Adolescente")
    elif idade < 60:
        print("Faixa etaria: Adulto")
    else:
        print("Faixa etaria: Idoso")

def analisar_contato(idade, email):
    """Analisa as informacoes de contato."""
    if idade >= 18 and "@" in email:
        print("Contato: completo")
    elif idade >= 18:
        print("Contato: e-mail invalido")
    else:
        print("Contato: menor de idade")

def analisar_email(email):
    """Analisa o provedor de e-mail."""
    if "@" not in email:
        print("E-mail invalido")
    elif email.endswith("@gmail.com"):
        print("Provedor: Gmail")
    elif email.endswith("@outlook.com"):
        print("Provedor: Outlook")
    else:
        print("Provedor: Outro")

def analisar_pessoa(cadastro):
    """Analisa uma pessoa cadastrada e exibe informacoes adicionais."""
    procurado = input("Nome para analisar: ")
    pessoa = cadastro.buscar_por_nome(procurado)

    if pessoa is None:
        print("Pessoa nao encontrada")
    else:
        analisar_faixa_etaria(pessoa.get_idade())
        analisar_email(pessoa.get_email())
        analisar_contato(
            pessoa.get_idade(),
            pessoa.get_email()
        )

def executar():
    """Executa o programa principal."""
    cadastro_pessoas = CadastroPessoas()
    op = 0

    while op != 6:
        op = exibir_menu()
        if op == 1:
            cadastrar_pessoa(cadastro_pessoas)
        elif op == 2:
            consultar_pessoa(cadastro_pessoas)
        elif op == 3:
            alterar_pessoa(cadastro_pessoas)
        elif op == 4:
            listar_pessoas(cadastro_pessoas)
        elif op == 5:
            analisar_pessoa(cadastro_pessoas)

    print("Fim do programa")

if __name__ == "__main__":
    executar()
