"""Representa uma pessoa cadastrada."""


class Pessoa:
    """Armazena os dados de uma pessoa."""

    def __init__(self, nome, idade, email):
        """Inicializa uma pessoa."""
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    def get_nome(self):
        """Retorna o nome da pessoa."""
        return self.__nome

    def get_idade(self):
        """Retorna a idade da pessoa."""
        return self.__idade

    def get_email(self):
        """Retorna o e-mail da pessoa."""
        return self.__email

    def set_nome(self, nome):
        """Altera o nome da pessoa."""
        self.__nome = nome

    def set_idade(self, idade):
        """Altera a idade da pessoa."""
        self.__idade = idade

    def set_email(self, email):
        """Altera o e-mail da pessoa."""
        self.__email = email
