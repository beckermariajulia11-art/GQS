""" Sistema de Cadastro de Pessoas - versao 2 """
# novos requisitos: menu, consulta, alteracao e listagem

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

def cadastrar_pessoa(lista_nomes, lista_idades, lista_emails):
    """Cadastra uma nova pessoa nas listas."""
    nome = input("Informe o nome: ")
    lista_nomes.append(nome)
    idade = int(input("Informe a idade: "))
    lista_idades.append(idade)
    email = input("Informe o email: ")
    lista_emails.append(email)
    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def consultar_pessoa(lista_nomes, lista_idades, lista_emails):
    """Consulta uma pessoa pelo nome."""
    procurado = input("Nome para consultar: ")
    pos = buscar_pessoa(lista_nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        exibir_pessoa(lista_nomes, lista_idades, lista_emails, pos)

def alterar_pessoa(lista_nomes, lista_idades, lista_emails):
    """Altera os dados de uma pessoa existente."""
    procurado = input("Nome para alterar: ")
    pos = buscar_pessoa(lista_nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        lista_nomes[pos] = input("Novo nome: ")
        lista_idades[pos] = int(input("Nova idade: "))
        lista_emails[pos] = input("Novo e-mail: ")
        print("Pessoa alterada com sucesso!")
        exibir_pessoa(lista_nomes, lista_idades, lista_emails, pos)

def exibir_pessoa(lista_nomes, lista_idades, lista_emails, pos):
    """Exibe os dados de uma pessoa."""
    print("Nome: " + lista_nomes[pos])
    print("Idade: " + str(lista_idades[pos]))
    print("E-mail: " + lista_emails[pos])
    if lista_idades[pos] >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def listar_pessoas(lista_nomes, lista_idades, lista_emails):
    """Lista todas as pessoas cadastradas."""
    if len(lista_nomes) == 0:
        print("Nenhuma pessoa cadastrada")
    pos = 0
    while pos < len(lista_nomes):
        exibir_pessoa(lista_nomes, lista_idades, lista_emails, pos)
        print("-------------------------")
        pos = pos + 1
    print("Total: " + str(len(lista_nomes)))

def buscar_pessoa(lista_nomes, nome_procurado):
    """Busca uma pessoa pelo nome e retorna sua posicao."""
    pos = 0
    while pos < len(lista_nomes):
        if lista_nomes[pos] == nome_procurado:
            return pos
        pos = pos + 1
    return -1

def classificar_faixa_etaria(idade):
    """Classifica uma pessoa com base em sua idade."""
    if idade < 12:
        return "Crianca"
    if idade < 18:
        return "Adolescente"
    if idade < 30:
        return "Adulto jovem"
    if idade < 60:
        return "Adulto"
    return "Idoso"

def avaliar_email(email):
    """Avalia se o e-mail informado pode ser utilizado."""
    if email == "":
        return "Cadastro incompleto: sem e-mail"
    if "@" not in email:
        return "E-mail invalido"
    return "E-mail utilizavel"

def identificar_provedor(email):
    """Identifica o provedor do e-mail informado."""
    if email.endswith("@gmail.com"):
        return "Gmail"
    if email.endswith("@outlook.com"):
        return "Outlook"
    if email.endswith("@hotmail.com"):
        return "Hotmail"
    if email.endswith("@utfpr.edu.br"):
        return "UTFPR"
    return "Outro"

def definir_condicao_contato(idade, email):
    """Define a condicao de contato com base na idade e no e-mail."""
    if idade >= 18 and email != "":
        return "Cadastro apto para contato"
    if idade >= 18 and email == "":
        return "Maior de idade sem contato"
    if idade < 18 and email != "":
        return "Menor de idade com contato"
    return "Menor de idade sem contato"
def analisar_pessoa(lista_nomes, lista_idades, lista_emails):
    """Analisa uma pessoa cadastrada e exibe informacoes adicionais."""
    procurado = input("Nome para analisar: ")
    pos = buscar_pessoa(lista_nomes, procurado)
    if pos == -1:
        print("Pessoa nao encontrada")
    else:
        idade = lista_idades[pos]
        email = lista_emails[pos]

        faixa_etaria = classificar_faixa_etaria(idade)
        print("Faixa etaria: " + faixa_etaria)

        avaliacao_email = avaliar_email(email)
        print(avaliacao_email)
        if email != "" and "@" in email:
            print("Provedor: " + identificar_provedor(email))
        condicao_contato = definir_condicao_contato(idade, email)
        print(condicao_contato)

nomes = []
idades = []
emails = []

op = 0
while op != 6:
    op = exibir_menu()
    if op == 1:
        cadastrar_pessoa(nomes, idades, emails)
    elif op == 2:
        consultar_pessoa(nomes, idades, emails)
    elif op == 3:
        alterar_pessoa(nomes, idades, emails)

    elif op == 4:
        listar_pessoas(nomes, idades, emails)
    elif op == 5:
        analisar_pessoa(nomes, idades, emails)
    elif op == 6:
        print("Saindo do programa...")

    else:
        print("Opcao invalida")
print("Fim do programa")
