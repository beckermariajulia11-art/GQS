
"""Implementação do repositório de pessoas usando MySQL."""

from typing import List, Optional

from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas
from conexao import conectar


class RepositorioPessoasMySQL(RepositorioPessoas):
    """Armazena e consulta pessoas em um banco de dados MySQL."""

    def cadastrar(self, pessoa: Pessoa) -> None:
        """Insere uma pessoa no banco de dados."""
        conexao = conectar()
        cursor = conexao.cursor()

        try:
            sql = """
                INSERT INTO pessoa (nome, idade, email)
                VALUES (%s, %s, %s)
            """
            valores = (
                pessoa.getNome(),
                pessoa.getIdade(),
                pessoa.getEmail()
            )

            cursor.execute(sql, valores)
            conexao.commit()

        finally:
            cursor.close()
            conexao.close()

    def buscar(self, nome: str) -> Optional[Pessoa]:
        """Busca a primeira pessoa com o nome informado."""
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        try:
            sql = """
                SELECT nome, idade, email
                FROM pessoa
                WHERE nome = %s
                ORDER BY id
                LIMIT 1
            """

            cursor.execute(sql, (nome,))
            resultado = cursor.fetchone()

            if resultado is None:
                return None

            return Pessoa(
                resultado["nome"],
                resultado["idade"],
                resultado["email"]
            )

        finally:
            cursor.close()
            conexao.close()

    def listar(self) -> List[Pessoa]:
        """Retorna todas as pessoas cadastradas."""
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        try:
            sql = """
                SELECT nome, idade, email
                FROM pessoa
                ORDER BY id
            """

            cursor.execute(sql)
            resultados = cursor.fetchall()

            return [
                Pessoa(item["nome"], item["idade"], item["email"])
                for item in resultados
            ]

        finally:
            cursor.close()
            conexao.close()

    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Altera a primeira pessoa encontrada pelo nome."""
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        try:
            cursor.execute(
                """
                SELECT id
                FROM pessoa
                WHERE nome = %s
                ORDER BY id
                LIMIT 1
                """,
                (nome,)
            )

            resultado = cursor.fetchone()

            if resultado is None:
                return False

            cursor.execute(
                """
                UPDATE pessoa
                SET nome = %s, idade = %s, email = %s
                WHERE id = %s
                """,
                (
                    nova_pessoa.getNome(),
                    nova_pessoa.getIdade(),
                    nova_pessoa.getEmail(),
                    resultado["id"]
                )
            )

            conexao.commit()
            return True

        finally:
            cursor.close()
            conexao.close()
