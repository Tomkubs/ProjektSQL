import sqlite3
def test_update_data():
    update_data()
    # Sprawdź czy dane zostały zaktualizowane w tabeli Klienci
    cursor.execute("SELECT Imie FROM Klienci WHERE ID = 1")
    assert cursor.fetchone()[0] == 'Janusz'

    # Sprawdź czy dane zostały zaktualizowane w tabeli Zamowienia
    cursor.execute("SELECT Kwota FROM Zamowienia WHERE ID = 1")
    assert cursor.fetchone()[0] == 200.00

    # Sprawdź czy dane zostały zaktualizowane w tabeli Produkty
    cursor.execute("SELECT Cena FROM Produkty WHERE ID = 1")
    assert cursor.fetchone()[0] == 120.00

    # Sprawdź czy dane zostały zaktualizowane w tabeli PozycjeZamowienia
    cursor.execute("SELECT Ilosc FROM PozycjeZamowienia WHERE ID = 1")
    assert cursor.fetchone()[0] == 3

test_update_data()