
"""Testes de integração do repositório MySQL."""

from uuid import uuid4

from conexao import conectar
from pessoa import Pessoa
from repositorio_pessoas_mysql import RepositorioPessoasMySQL


def test_operacoes_repositorio_mysql():
    """Testa cadastro, busca, listagem e alteração no MySQL."""
    repositorio = RepositorioPessoasMySQL()

    identificador = uuid4().hex[:8]
    nome = f"Teste {identificador}"
    novo_nome = f"Alterado {identificador}"
    email = f"teste_{identificador}@exemplo.com"
    novo_email = f"alterado_{identificador}@exemplo.com"

    try:
        # Cadastro
        pessoa = Pessoa(nome, 25, email)
        repositorio.cadastrar(pessoa)

        # Busca
        encontrada = repositorio.buscar(nome)

        assert encontrada is not None
        assert encontrada.get_nome() == nome
        assert encontrada.get_idade() == 25
        assert encontrada.get_email() == email

        # Listagem
        pessoas = repositorio.listar()

        assert any(
            item.get_email() == email
            for item in pessoas
        )

        # Alteração
        nova_pessoa = Pessoa(novo_nome, 30, novo_email)

        assert repositorio.alterar(nome, nova_pessoa) is True

        alterada = repositorio.buscar(novo_nome)

        assert alterada is not None
        assert alterada.get_idade() == 30
        assert alterada.get_email() == novo_email

        # Busca inexistente
        assert repositorio.buscar(nome) is None

        # Alteração de pessoa inexistente
        assert repositorio.alterar(
            "Pessoa inexistente",
            nova_pessoa
        ) is False

    finally:
        # Remove os registros criados pelo teste.
        conexao = conectar()
        cursor = conexao.cursor()

        try:
            cursor.execute(
                """
                DELETE FROM pessoa
                WHERE email IN (%s, %s)
                """,
                (email, novo_email)
            )
            conexao.commit()
        finally:
            cursor.close()
            conexao.close()
