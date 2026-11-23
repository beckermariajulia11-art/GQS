"""Testes da conexão com o banco de dados."""

from conexao import conectar

def test_conexao_mysql():
    """Verifica se é possível conectar ao MySQL."""
    conexao = conectar()

    assert conexao.is_connected()

    conexao.close()
