
from distutils.util import execute
import sqlite3
from statistics import geometric_mean
import tkinter as tk
from tkinter import messagebox

# Tworzenie połączenia z bazą danych
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def create_table():
    # Tworzenie tabeli Klienci
    cursor.execute("""CREATE TABLE IF NOT EXISTS Klienci (
                     ID INTEGER PRIMARY KEY,
                     Imie TEXT,
                     Nazwisko TEXT,
                     Email TEXT,
                     NrTelefonu TEXT );""")
    
    # Tworzenie tabeli Zamowienia
    cursor.execute("""CREATE TABLE IF NOT EXISTS Zamowienia (
                    ID INTEGER PRIMARY KEY,
                    KlientID INTEGER,
                    DataZamowienia TEXT,
                    Kwota REAL,
                    IloscProduktow INTEGER,
                    FOREIGN KEY (KlientID) REFERENCES Klienci(ID));""")
    
    # Tworzenie tabeli Produkty
    cursor.execute("""CREATE TABLE IF NOT EXISTS Produkty (
                    ID INTEGER PRIMARY KEY,
                    NazwaProduktu TEXT,
                    Cena REAL,
                    Kolekcja TEXT,
                    Material TEXT);""")
    
    # Tworzenie tabeli PozycjeZamowienia
    cursor.execute("""CREATE TABLE IF NOT EXISTS PozycjeZamowienia (
                    ID INTEGER PRIMARY KEY,
                    ZamowienieID INTEGER,
                    ProduktID INTEGER,
                    Ilosc INTEGER,
                    FOREIGN KEY (ZamowienieID) REFERENCES Zamowienia(ID),
                    FOREIGN KEY (ProduktID) REFERENCES Produkty(ID));""")
    
    conn.commit()
    messagebox.showinfo("Informacja", "Tabele zostały utworzone.")


def insert_data():
    # Dodawanie przykładowych danych do tabeli Klienci
    person = [
        (1, 'Jan', 'Kowalski', 'jan.kowalski@example.com', '543 712 899'),
        (2, 'Anna', 'Nowak', 'anna.nowak@example.com', '877 326 741'),
        (3, 'Adam', 'Wrzeciono', 'adam.wrzeciono@example.com', '764 182 954'),
        (4, 'Wojciech', 'Kowalczyk', 'wojciech.kowalczyk@example.com', '874 126 562'),
        (5, 'Marta', 'Krakowska', 'marta.krakowska@example.com', '987 436 312')
    ]
    cursor.executemany("INSERT INTO Klienci (ID, Imie, Nazwisko, Email, NrTelefonu) VALUES (?,?,?,?,?)", person)
    
    # Dodawanie przykładowych danych do tabeli Zamowienia
    zamowienie = [
        (1, 1, '2023-06-26', 100.00, 1),
        (2, 2, '2023-06-27', 150.00, 1),
        (3, 3, '2023-06-28', 300.00, 3),
        (4, 4, '2023-06-29', 300.00, 2),
        (5, 5, '2023-06-30', 400.00, 2)
    ]
    cursor.executemany("INSERT INTO Zamowienia (ID, KlientID, DataZamowienia, Kwota, IloscProduktow) VALUES (?,?,?,?,?)", zamowienie)
    
    # Dodawanie przykładowych danych do tabeli Produkty
    produkt = [
        (1, 'Koszulka', 100.00, 'Lato', 'Bawelna'),
        (2, 'Spodnie', 150.00, 'Wiosna', 'Jeans'),
        (3, 'Bluza', 200.00, 'Jesien', 'Bawelna'),
        (4, 'Koszula', 170.00, 'Lato', 'Len'),
        (5, 'Skarpetki', 50.00, 'Caloroczne', 'Bawelna')
    ]
    cursor.executemany("INSERT INTO Produkty (ID, NazwaProduktu, Cena, Kolekcja, Material) VALUES (?,?,?,?,?)", produkt)
    
    # Dodawanie przykładowych danych do tabeli PozycjeZamowienia
    pozycja = [
        (1, 1, 1, 2),
        (2, 2, 2, 1),
        (3, 3, 3, 1),
        (4, 4, 4, 1),
        (5, 5, 5, 1)
    ]
    cursor.executemany("INSERT INTO PozycjeZamowienia (ID, ZamowienieID, ProduktID, Ilosc,) VALUES (?,?,?,?)", pozycja)
    
    conn.commit()
    messagebox.showinfo("Informacja", "Dane zostały dodane do tabel.")


def show_data():
    # Pobieranie danych z tabeli Klienci
    cursor.execute("SELECT * FROM Klienci")
    klienci_data = cursor.fetchall()
    
    # Pobieranie danych z tabeli Zamowienia
    cursor.execute("SELECT * FROM Zamowienia")
    zamowienia_data = cursor.fetchall()
    
    # Pobieranie danych z tabeli Produkty
    cursor.execute("SELECT * FROM Produkty")
    produkty_data = cursor.fetchall()
    
    # Pobieranie danych z tabeli PozycjeZamowienia
    cursor.execute("SELECT * FROM PozycjeZamowienia")
    pozycje_zamowienia_data = cursor.fetchall()
    
    # Wyświetlanie danych
    messagebox.showinfo("Klienci", klienci_data)
    messagebox.showinfo("Zamowienia", zamowienia_data)
    messagebox.showinfo("Produkty", produkty_data)
    messagebox.showinfo("PozycjeZamowienia", pozycje_zamowienia_data)


def update_data():
    # Aktualizacja danych w tabeli Klienci
    cursor.execute("UPDATE Klienci SET Imie = 'Janusz' WHERE ID = 1")
    
    # Aktualizacja danych w tabeli Zamowienia
    cursor.execute("UPDATE Zamowienia SET Kwota = 200.00 WHERE ID = 1")
    
    # Aktualizacja danych w tabeli Produkty
    cursor.execute("UPDATE Produkty SET Cena = 120.00 WHERE ID = 1")
    
    # Aktualizacja danych w tabeli PozycjeZamowienia
    cursor.execute("UPDATE PozycjeZamowienia SET Ilosc = 3 WHERE ID = 1")
    
    conn.commit()
    messagebox.showinfo("Informacja", "Dane zostały zaktualizowane.")


def delete_data():
    # Usunięcie danych z tabeli Klienci
    cursor.execute("DELETE FROM Klienci WHERE ID = 5")
    
    # Usunięcie danych z tabeli Zamowienia
    cursor.execute("DELETE FROM Zamowienia WHERE ID = 5")
    
    # Usunięcie danych z tabeli Produkty
    cursor.execute("DELETE FROM Produkty WHERE ID = 5")
    
    # Usunięcie danych z tabeli PozycjeZamowienia
    cursor.execute("DELETE FROM PozycjeZamowienia WHERE ID = 5")
    
    conn.commit()
    messagebox.showinfo("Informacja", "Dane zostały usunięte.")


# Tworzenie głównego okna aplikacji
window = tk.Tk()
window.title("Aplikacja obsługująca bazę danych")
window.geometry ("700x450")
window ['background']='#CC99CC'




# Tworzenie przycisków
create_table_button = tk.Button(window, text="Utwórz tabele",bg='#FFF0F5',activebackground='#FF0099', command=create_table)
create_table_button.pack()
create_table_button.config (height=2, width=20)
create_table_button.place (x=280, y=100)

insert_data_button = tk.Button(window, text="Dodaj dane",bg='#FFF0F5',activebackground='#FF0099', command=insert_data)
insert_data_button.pack()
insert_data_button.config (height=2, width=20)
insert_data_button.place (x=280, y=150)

show_data_button = tk.Button(window, text="Wyświetl dane",bg='#FFF0F5',activebackground='#FF0099', command=show_data)
show_data_button.pack()
show_data_button.config (height=2, width=20)
show_data_button.place (x=280, y=200)

update_data_button = tk.Button(window, text="Aktualizuj dane", bg='#FFF0F5',activebackground='#FF0099',  command=update_data)
update_data_button.pack()
update_data_button.config (height=2, width=20)
update_data_button.place (x=280, y=250)


delete_data_button = tk.Button(window, text="Usuń dane",bg='#FFF0F5', activebackground='#FF0099', command=delete_data)
delete_data_button.pack()
delete_data_button.config (height=2, width=20)
delete_data_button.place (x=280, y=300)




window.mainloop()
