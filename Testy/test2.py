import sqlite3
def test_insert_data():
    insert_data()
    # Sprawdź czy dane zostały dodane do tabeli Klienci
    cursor.execute("SELECT COUNT(*) FROM Klienci")
    assert cursor.fetchone()[0] == 5

    # Sprawdź czy dane zostały dodane do tabeli Zamowienia
    cursor.execute("SELECT COUNT(*) FROM Zamowienia")
    assert cursor.fetchone()[0] == 5

    # Sprawdź czy dane zostały dodane do tabeli Produkty
    cursor.execute("SELECT COUNT(*) FROM Produkty")
    assert cursor.fetchone()[0] == 5

    # Sprawdź czy dane zostały dodane do tabeli PozycjeZamowienia
    cursor.execute("SELECT COUNT(*) FROM PozycjeZamowienia")
    assert cursor.fetchone()[0] == 5

test_insert_data()