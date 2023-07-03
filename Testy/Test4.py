import sqlite3
def test_delete_data():
    delete_data()
    # Sprawdź czy dane zostały usunięte z tabeli Klienci
    cursor.execute("SELECT COUNT(*) FROM Klienci WHERE ID = 5")
    assert cursor.fetchone()[0] == 0

    # Sprawdź czy dane zostały usunięte z tabeli Zamowienia
    cursor.execute("SELECT COUNT(*) FROM Zamowienia WHERE ID = 5")
    assert cursor.fetchone()[0] == 0

    # Sprawdź czy dane zostały usunięte z tabeli Produkty
    cursor.execute("SELECT COUNT(*) FROM Produkty WHERE ID = 5")
    assert cursor.fetchone()[0] == 0

    # Sprawdź czy dane zostały usunięte z tabeli PozycjeZamowienia
    cursor.execute("SELECT COUNT(*) FROM PozycjeZamowienia WHERE ID = 5")
    assert cursor.fetchone()[0] == 0

test_delete_data()