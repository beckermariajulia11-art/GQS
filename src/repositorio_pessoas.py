"""Contrato de persistência do cadastro de pessoas."""

from abc import ABC, abstractmethod
from typing import List, Optional

from pessoa import Pessoa


class RepositorioPessoas(ABC):
    """Interface que toda forma de armazenamento deve cumprir."""

    @abstractmethod
    def cadastrar(self, pessoa: Pessoa) -> None:
        """Armazena uma nova pessoa."""

    @abstractmethod
    def buscar(self, nome: str) -> Optional[Pessoa]:
        """Devolve a primeira pessoa com o nome informado, ou None."""

    @abstractmethod
    def listar(self) -> List[Pessoa]:
        """Devolve todas as pessoas, na ordem de cadastro."""

    @abstractmethod
    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Substitui os dados da pessoa; True se encontrou, senão False."""
