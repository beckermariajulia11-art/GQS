"""Testes das operações de cadastro."""

from cadastro import CadastroPessoas

def test_cadastrar_pessoa():
    """Confere armazenamento e quantidade."""
    cadastro_pessoas = CadastroPessoas()
    cadastro_pessoas.cadastrar("Ana", 20, "ana@example.com")
    pessoas = cadastro_pessoas.listar()
    assert len(pessoas) == 1
    assert pessoas[0].get_nome() == "Ana"
    assert pessoas[0].get_idade() == 20
    assert pessoas[0].get_email() == "ana@example.com"

def test_buscar_por_nome():
    """Encontra uma pessoa já cadastrada."""
    cadastro_pessoas = CadastroPessoas()
    cadastro_pessoas.cadastrar("Ana", 20, "ana@example.com")
    encontrada = cadastro_pessoas.buscarPorNome("Ana")
    assert encontrada is not None
    assert encontrada.get_nome() == "Ana"
    assert encontrada.get_idade() == 20
    assert encontrada.get_email() == "ana@example.com"
