import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors
import sqlite3






#----DATA


def fetch_data():
    try:
        with sqlite3.connect("studenci.db") as database:
            mycursor = database.cursor()
            mycursor.execute("""
                SELECT o.IdOcena, s.imie, s.Nazwisko, p.Nazwa, o.[Ocena]
                FROM Student AS s
                JOIN Ocena AS o ON o.IdStudent=s.IdStudent
                JOIN Przedmiot AS p ON p.IdPrzedmiot = o.IdPrzedmiot
            """)

            result = mycursor.fetchall()
            database.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")
        result = None

    return result


def load_data():
    data = fetch_data()
    treeview.delete(*treeview.get_children())
    for row in data:
        values = row[:5]
        treeview.insert("", "end", values=values)



#-----window

def open_new_book_window():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj nową ocene")

    labels = ["Imie:", "Nazwisko:", "Nazwa przedmiotu:", "Ocena"]
    entries = []

    for label_text in labels:
        label = ttk.Label(new_window, text=label_text)
        label.pack()
        entry = ttk.Entry(new_window)
        entry.pack()
        entries.append(entry)

    def add_new():
        values = [entry.get() for entry in entries]

        try:
            with sqlite3.connect("studenci.db") as database:
                mycursor = database.cursor()

                mycursor.execute("SELECT Nazwa FROM Przedmiot WHERE Nazwa = (?)", (values[2],))
                if mycursor.fetchall() == []:
                    mycursor.execute("INSERT INTO Przedmiot (Nazwa) VALUES (?)", (values[2],))

                mycursor.execute("SELECT Imie, Nazwisko FROM Student WHERE Imie == (?) AND Nazwisko == (?)",
                                 (values[0], values[1]))
                if mycursor.fetchall() == []:
                    mycursor.execute("INSERT INTO Student (Imie, Nazwisko) VALUES (?, ?)", (values[0], values[1]))

                mycursor.execute("SELECT IdStudent FROM Student WHERE Imie == (?) AND Nazwisko == (?)",
                                 (values[0], values[1]))
                IdStudent = mycursor.fetchall()[0][0]

                mycursor.execute("SELECT IdPrzedmiot FROM Przedmiot WHERE Nazwa == (?)", (values[2],))
                IdPrzedmiot = mycursor.fetchall()[0][0]

                mycursor.execute("INSERT INTO Ocena (IdStudent, IdPrzedmiot, Ocena) VALUES (?, ?, ?)",
                                 (IdStudent, IdPrzedmiot, values[3]))

                database.commit()

        except sqlite3.Error as e:
            print(f"Error: {e}")

        load_data()
        new_window.destroy()

    add_button = ttk.Button(new_window, text="Dodaj", command=add_new)
    add_button.pack()


def open_details_window(event):
    selected_item = treeview.focus()

    if selected_item:
        item_data = treeview.item(selected_item)
        item_values = item_data["values"]

        details_window = tk.Toplevel(root)
        details_window.title("Szczegóły")

        labels = ["ID:", "Imie:", "Nazwisko:", "Przedmiot:", "Ocena:"]
        entries = []

        for i in range(len(labels)):
            label_text = labels[i]
            value = item_values[i]

            label = ttk.Label(details_window, text=label_text)
            label.pack()

            entry = ttk.Entry(details_window)
            entry.insert(0, value)
            if label_text == "ID:":
                entry.config(state="disabled")
            entry.pack()

            entries.append(entry)

        def delete_data():
            try:
                mydb = sqlite3.connect("studenci.db")
                mycursor = mydb.cursor()
                mycursor.execute("DELETE FROM Ocena WHERE idOcena = (?)", (entries[0].get(),))
                mydb.commit()
            except sqlite3.Error as e:
                print(f"Error: {e}")
            finally:
                if mycursor:
                    mycursor.close()
                if mydb:
                    mydb.close()
            load_data()

        delete_button = ttk.Button(details_window, text="Usuń Ocene", command=delete_data)
        delete_button.pack()

        def update_data():
            try:
                mydb = sqlite3.connect("studenci.db")
                mycursor = mydb.cursor()

                mycursor.execute(
                    "SELECT p.IdPrzedmiot FROM Przedmiot AS p JOIN Ocena AS o ON p.IdPrzedmiot=o.IdPrzedmiot WHERE o.IdOcena = (?)",
                    (entries[0].get(),)
                )
                result = mycursor.fetchall()
                if result:
                    mycursor.execute(
                        "UPDATE Przedmiot SET Nazwa = (?) WHERE IdPrzedmiot = (?)",
                        (entries[3].get(), result[0][0])
                    )

                mycursor.execute(
                    "SELECT s.IdStudent FROM Student AS s JOIN Ocena AS o ON s.IdStudent=o.IdStudent WHERE o.IdOcena = (?)",
                    (entries[0].get(),)
                )
                result = mycursor.fetchall()
                if result:
                    mycursor.execute(
                        "UPDATE Student SET Imie = (?), Nazwisko = (?) WHERE IdStudent = (?)",
                        (entries[1].get(), entries[2].get(), result[0][0])
                    )
                mycursor.execute(
                    "UPDATE Ocena SET Ocena = (?) WHERE IdOcena = (?)",
                    (entries[4].get(), entries[0].get())
                )
                mydb.commit()
            except sqlite3.Error as e:
                print(f"Error: {e}")
            finally:
                if mycursor:
                    mycursor.close()
                if mydb:
                    mydb.close()
            load_data()

        update_button = ttk.Button(details_window, text="Zaaktualizuj informacje", command=update_data)
        update_button.pack()


root = tk.Tk()
root.configure(bg='black')
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height

root.title()
root.geometry(f"{int(screen_width)}x{int(screen_height)}")
root.iconbitmap("./bookshelf.ico")

treeview = ttk.Treeview(root)
treeview["columns"] = ("id", "imie", "nazwisko", "przedmiot", "ocena")
treeview.pack()
treeview.heading("id", text="Id")
treeview.heading("imie", text="Imie")
treeview.heading("nazwisko", text="Nazwisko")
treeview.heading("przedmiot", text="Przedmiot")
treeview.heading("ocena", text="Ocena")
treeview.column("#0", width=200)

add_new_book_button = tk.Button(root, text="Dodaj nową ocene", command=open_new_book_window)
add_new_book_button.pack()
treeview.bind("<Double-1>", open_details_window)
load_data()
root.mainloop()
