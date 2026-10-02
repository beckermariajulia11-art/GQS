"""Gerenciamento de Cadastro de Pessoas."""

from pessoa import Pessoa


class CadastroPessoas:
    """Mantém e gerencia o conjunto de pessoas cadastradas."""

    def __init__(self):
        """Inicializa o cadastro vazio."""
        self.__pessoas = []

    def cadastrar(self, nome, idade, email):
        """Cadastra uma nova pessoa."""
        pessoa = Pessoa(nome, idade, email)
        self.__pessoas.append(pessoa)
        return pessoa

    def buscar_por_nome(self, nome_procurado):
        """Busca uma pessoa pelo nome."""
        for pessoa in self.__pessoas:
            if pessoa.get_nome() == nome_procurado:
                return pessoa
        return None

    def listar(self):
        """Retorna todas as pessoas cadastradas."""
        return self.__pessoas

    def alterar(self, pessoa, novo_nome, nova_idade, novo_email):
        """Altera os dados de uma pessoa."""
        pessoa.set_nome(novo_nome)
        pessoa.set_idade(nova_idade)
        pessoa.set_email(novo_email)

        return pessoa
