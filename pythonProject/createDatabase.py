import sqlite3

db = sqlite3.connect("studenci.db")
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE Ocena (
        IdStudent int NOT NULL,
        IdPrzedmiot int NOT NULL,
        Ocena varchar(3) NOT NULL,
        CONSTRAINT Ocena_pk PRIMARY KEY (IdStudent,IdPrzedmiot),
        CONSTRAINT Ocena_Student FOREIGN KEY (IdStudent)
        REFERENCES Student (IdStudent),
        CONSTRAINT Ocena_Przedmiot FOREIGN KEY (IdPrzedmiot)
        REFERENCES Przedmiot (IdPrzedmiot)
    );
''')

cursor.execute('''
    CREATE TABLE Przedmiot (
        IdPrzedmiot int NOT NULL CONSTRAINT Przedmiot_pk PRIMARY KEY,
        Nazwa varchar(30) NOT NULL
    );
''')
cursor.execute('''
    CREATE TABLE Student (
        IdStudent double precision NOT NULL CONSTRAINT Student_pk PRIMARY KEY,
        Imie varchar(30) NOT NULL,
        Nazwisko varchar(30) NOT NULL
    );
''')
db.commit()
db.close()