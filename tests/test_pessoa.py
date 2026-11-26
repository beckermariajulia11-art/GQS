from pessoa import Pessoa


def test_alterar_idade():
    pessoa = Pessoa("Ana", 20, "ana@example.com")

    pessoa.set_idade(21)

    assert pessoa.get_idade() == 21
