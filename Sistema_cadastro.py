# Sistema de Cadastro de Pessoas - versao 2
# novos requisitos: menu, consulta, alteracao e listagem

def exibir_menu():
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

def cadastrar_pessoa(nomes, idades, emails):
    nome = input("Informe o nome: ")
    nomes.append(nome)
    idade = int(input("Informe a idade: "))
    idades.append(idade)
    email = input("Informe o email: ")
    emails.append(email)
    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def consultar_pessoa(nomes, idades, emails):
    procurado = input("Nome para consultar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        exibir_pessoa(nomes, idades, emails, pos)

def alterar_pessoa(nomes, idades, emails):
    procurado = input("Nome para alterar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        nomes[pos] = input("Novo nome: ")
        idades[pos] = int(input("Nova idade: "))
        emails[pos] = input("Novo e-mail: ")
        print("Pessoa alterada com sucesso!")
        exibir_pessoa(nomes, idades, emails, pos)

def exibir_pessoa(nomes, idades, emails, pos):
    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])
    if idades[pos] >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def listar_pessoas(nomes, idades, emails):
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada")
    pos = 0
    while pos < len(nomes):
        exibir_pessoa(nomes, idades, emails, pos)
        print("-------------------------")
        pos = pos + 1
    print("Total: " + str(len(nomes)))

def buscar_pessoa(nomes, nome_procurado):
    pos = 0
    while pos < len(nomes):
        if nomes[pos] == nome_procurado:
            return pos
        pos = pos + 1
    return -1

def classificar_faixa_etaria(idade):
    if idade < 12:
        return "Crianca"
    elif idade < 18:
        return "Adolescente"
    elif idade < 30:
        return "Adulto jovem"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"

def avaliar_email(email):
    if email == "":
        return "Cadastro incompleto: sem e-mail"
    elif "@" not in email:
        return "E-mail invalido"
    else:
        return "E-mail utilizavel"

def identificar_provedor(email):
    if email.endswith("@gmail.com"):
        return "Gmail"
    elif email.endswith("@outlook.com"):
        return "Outlook"
    elif email.endswith("@hotmail.com"):
        return "Hotmail"
    elif email.endswith("@utfpr.edu.br"):
        return "UTFPR"
    else:
        return "Outro"

def definir_condicao_contato(idade, email):
    if idade >= 18 and email != "":
        return "Cadastro apto para contato"
    elif idade >= 18 and email == "":
        return "Maior de idade sem contato"
    elif idade < 18 and email != "":
        return "Menor de idade com contato"
    else:
        return "Menor de idade sem contato"
    
def analisar_pessoa(nomes, idades, emails):
    procurado = input("Nome para analisar: ")
    pos = buscar_pessoa(nomes, procurado)

    if pos == -1:
        print("Pessoa nao encontrada")
    else:
        idade = idades[pos]
        email = emails[pos]

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

qtd = 0
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