
"""Configuração de conexão com o banco de dados MySQL."""

import os

import mysql.connector


def conectar():
    """Abre e retorna uma conexão com o MySQL."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3307")),
        database=os.getenv("DB_NAME", "cadastro"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root_lab_2026"),
    )
