"""Gerenciamento do cadastro de pessoas."""

from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas


class CadastroPessoas:
    """Regras de negócio do cadastro; o armazenamento é delegado ao repositório."""

    def __init__(self, repositorio: RepositorioPessoas):
        """Inicializa o cadastro com o repositório fornecido."""
        self.__repositorio = repositorio

    def cadastrar(self, nome, idade, email):
        """Cadastra uma nova pessoa no repositório."""
        pessoa = Pessoa(nome, idade, email)
        self.__repositorio.cadastrar(pessoa)
        return pessoa

    def buscar_por_nome(self, nome_procurado):
        """Busca uma pessoa pelo nome."""
        return self.__repositorio.buscar(nome_procurado)

    def listar(self):
        """Retorna todas as pessoas cadastradas."""
        return self.__repositorio.listar()

    def alterar(self, pessoa_ou_nome, novo_nome, nova_idade, novo_email):
        """Altera os dados de uma pessoa existente."""
        nome_atual = (
            pessoa_ou_nome.get_nome()
            if isinstance(pessoa_ou_nome, Pessoa)
            else pessoa_ou_nome
        )
        nova_pessoa = Pessoa(novo_nome, nova_idade, novo_email)
        if self.__repositorio.alterar(nome_atual, nova_pessoa):
            return nova_pessoa
        return None
