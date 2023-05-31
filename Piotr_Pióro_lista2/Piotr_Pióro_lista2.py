import sqlite3
import ssl
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeaveOneOut, cross_val_score

ssl._create_default_https_context = ssl._create_unverified_context

# Wczytaj dane z adresu podanego w pliku tekstowym: pliktextowy.txt
# do ramki danych.
# Użyj reszty wierszy jako nagłówków ramki danych.
# Uwaga! Zobacz która zmienna jest zmienną objaśnianą, będzie to potrzebne do dalszych zadań.

with open('pliktextowy.txt') as file:
    url = file.readline().strip("\n")
    headers = [line.rstrip() for line in file]

df = pd.read_csv(url, names=headers)  # tutaj podmień df. Ma zawierać wczytane dane.

# Zadanie1 przypisz nazwy kolumn z df w jednej linii:   (2pkt)

wynik1 = df.columns.tolist()
print(wynik1)

# Zadanie 2: Wypisz liczbę wierszy oraz kolumn ramki danych w jednej linii.  (2pkt)
wynik2 = f"rows= {df.shape[0]}, columns= {df.shape[1]}"
print(wynik2)


# Zadanie Utwórz klasę Wine na podstawie wczytanego zbioru:
# wszystkie zmienne objaśniające powinny być w liscie.
# Zmienna objaśniana jako odrębne pole.
# metoda __init__ powinna posiadać 2 parametry:
# listę (zmienne objaśniające) oraz liczbę(zmienna objaśniana).
# nazwy mogą być dowolne.

# Klasa powinna umożliwiać stworzenie nowego obiektu na podstawie
# już istniejącego obiektu jak w pdf z lekcji lab6.
# podpowiedź: metoda magiczna __repr__
# Nie pisz metody __str__.

class Wine:
    def __init__(self, zmienne_objaśniajace, zmienna_objaśniana):
        self.zmienne_objaśniające = zmienne_objaśniajace
        self.zmienna_objaśniana = zmienna_objaśniana

    def __repr__(self):
        return f"Wine(zmienna_objaśniana={self.zmienna_objaśniana},zmienne_objaśniajace={self.zmienne_objaśniające})"


# Zadanie 3 Utwórz przykładowy obiekt:   (3pkt)

TypeOf = df.iloc[0, 0]
state = True
TypeOf_List = []

for i in range(len(df.iloc[1])):
    if state:
        state = False
        continue
    TypeOf_List.append(df.iloc[0, i])

wynik3 = Wine(TypeOf_List, TypeOf)  # do podmiany. Pamiętaj - ilość elementów, jak w zbiorze danych.
# Uwaga! Pamiętaj, która zmienna jest zmienną objaśnianą
print(wynik3)

# Zadanie 4.                             (3pkt)
# Zapisz wszystkie dane z ramki danych do listy obiektów typu Wine.
# Nie podmieniaj listy, dodawaj elementy.
##Uwaga! zobacz w jakiej kolejności podawane są zmienne objaśniające i objaśniana.
# Podpowiedź zobacz w pliktextowy.txt
wineList = []

for i in range(df.shape[0]):
    List = []
    TypeOf = df.iloc[i, 0]
    for j in range(1, df.shape[1]):
        List.append(df.iat[i, j])
    wineList.append(Wine(List, TypeOf))

wynik4 = len(wineList)
print(wynik4)

# Zadanie5 - Weź ostatni element z listy i na podstawie         (3pkt)
# wyniku funkcji repr utwórz nowy obiekt - eval(repr(obiekt))
# do wyniku przypisz zmienną objaśnianą z tego obiektu:

last = wineList[df.shape[0]-1]
wynik5 = eval(repr(last))
print(wynik5)

# Zadanie 6:                                                          (3pkt)
# Zapisz ramkę danych  do bazy SQLite nazwa bazy(dopisz swoje imię i nazwisko):
# wines_imie_nazwisko, nazwa tabeli: wines.
# Następnie wczytaj dane z tabeli wybierając z bazy danych tylko wiersze z typem wina nr 3
# i zapisz je do nowego data frame:


connection = sqlite3.connect('wines_Piotr_Pióro')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS wines;")
sql = f"CREATE TABLE IF NOT EXISTS wines ({', '.join(headers)} REAL)"

cursor.execute(sql)
connection.commit()

for i, row in df.iterrows():
    sql = f"INSERT INTO wines ({', '.join(headers)}) VALUES ({', '.join(map(str, row.values))})"
    cursor.execute(sql)
    connection.commit()

wynik6 = pd.read_sql_query("SELECT * FROM wines WHERE TypeOf = 3.0", connection)  # tutaj do podmiany

cursor.close()
connection.close()
print(wynik6.shape)

# Zadanie 7                                                          (1pkt)
# Utwórz model regresji Logistycznej z domyślnymi ustawieniami:

model = LogisticRegression()
wynik7 = model.__class__.__name__
print(wynik7)

# Zadanie 8:                                                        (3pkt)
# Dokonaj podziału ramki danych na dane objaśniające i  do klasyfikacji.
# Znormalizuj dane objaśniające za pomocą:
# X = preprocessing.normalize(X)
# Wytenuj model na wszystkich danych bez podziału na zbiór treningowy i testowy.
# Wykonaj sprawdzian krzyżowy, używając LeaveOneOut() zamiast KFold (Parametr cv)
#  Podaj średnią dokładność (accuracy)

x = df.iloc[:,1:].values.tolist()
y = df.iloc[:,0].values.tolist()

X = preprocessing.normalize(x)
model.fit(X, y)

leave_one_out = LeaveOneOut()
accuracy_score = cross_val_score(model, X, y, cv=leave_one_out, scoring="accuracy")

wynik8 = accuracy_score.mean()

print(wynik8)
