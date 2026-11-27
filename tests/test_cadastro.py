"""Testes das operações de cadastro."""

import copy

import pytest

from cadastro import CadastroPessoas
from pessoa import Pessoa
from repositorio_pessoas_memoria import RepositorioPessoasMemoria


def test_cadastrar_pessoa():
    """Confere armazenamento e quantidade."""
    cadastro = CadastroPessoas(RepositorioPessoasMemoria())
    cadastro.cadastrar("Ana", 20, "ana@example.com")

    pessoas = cadastro.listar()
    assert len(pessoas) == 1
    assert pessoas[0].get_nome() == "Ana"
    assert pessoas[0].get_idade() == 20
    assert pessoas[0].get_email() == "ana@example.com"


def test_buscar_por_nome():
    """Encontra uma pessoa já cadastrada."""
    cadastro = CadastroPessoas(RepositorioPessoasMemoria())
    cadastro.cadastrar("Ana", 20, "ana@example.com")
    encontrada = cadastro.buscar_por_nome("Ana")
    assert encontrada is not None
    assert encontrada.get_nome() == "Ana"
    assert encontrada.get_idade() == 20
    assert encontrada.get_email() == "ana@example.com"


class RepositorioDeCopias(RepositorioPessoasMemoria):  # pylint: disable=too-few-public-methods
    """Devolve cópias, simulando objetos reconstruídos."""

    def buscar(self, nome):
        """Busca e retorna uma cópia da pessoa encontrada."""
        pessoa = super().buscar(nome)
        if pessoa is None:
            return None
        return copy.copy(pessoa)

@pytest.mark.parametrize("fabrica", [RepositorioPessoasMemoria, RepositorioDeCopias])
def test_alterar_persiste(fabrica):
    """Garante que alterar() grava no repositório, mesmo com cópias."""
    repositorio = fabrica()
    repositorio.cadastrar(Pessoa("Ana Souza", 30, "ana@example.com"))

    cadastro = CadastroPessoas(repositorio)
    cadastro.alterar("Ana Souza", "Ana Souza", 31, "ana.s@example.com")

    pessoa = repositorio.buscar("Ana Souza")

    assert pessoa is not None
    assert pessoa.get_idade() == 31
    assert pessoa.get_email() == "ana.s@example.com"
