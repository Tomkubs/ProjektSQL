import sqlite3
from distutils.util import execute
def test_create_table():
    create_table()
    # Sprawdz czy tabela Klienci zostala utworzona
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Klienci'")
    assert cursor.fetchone() is not None

    # Sprawdz czy tabela Zamowienia zostala utworzona
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Zamowienia'")
    assert cursor.fetchone() is not None

    # Sprawdz czy tabela Produkty zostala utworzona
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Produkty'")
    assert cursor.fetchone() is not None

    # Sprawdz czy tabela PozycjeZamowienia zostala utworzona
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='PozycjeZamowienia'")
    assert cursor.fetchone() is not None

test_create_table()