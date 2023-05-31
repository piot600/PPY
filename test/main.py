import smtplib
from email.mime.text import MIMEText
from tkinter import *
from tkinter import messagebox

from tkscrolledframe import ScrolledFrame



def add_student():
    add_window = Toplevel()
    add_window.title("Dodaj studenta")

    email_label = Label(add_window, text="E-mail:")
    email_label.grid(row=0, column=0)
    email_entry = Entry(add_window)
    email_entry.grid(row=0, column=1)

    first_name_label = Label(add_window, text="Imię:")
    first_name_label.grid(row=1, column=0)
    first_name_entry = Entry(add_window)
    first_name_entry.grid(row=1, column=1)

    last_name_label = Label(add_window, text="Nazwisko:")
    last_name_label.grid(row=2, column=0)
    last_name_entry = Entry(add_window)
    last_name_entry.grid(row=2, column=1)

    points_label = Label(add_window, text="Punkty:")
    points_label.grid(row=3, column=0)
    points_entry = Entry(add_window)
    points_entry.grid(row=3, column=1)
    ocena_label = Label(add_window, text="Ocena:")
    ocena_label.grid(row=4, column=0)
    ocena_entry = Entry(add_window)
    ocena_entry.grid(row=4, column=1)
    status_label = Label(add_window, text="Status:")
    status_label.grid(row=5, column=0)
    status_entry = Entry(add_window)
    status_entry.grid(row=5, column=1)










def init_window():
    global sf_inner

    root = Tk()
    root.title("Lista studentów")
    global sf

    sf = ScrolledFrame(root, width=640, height=480)
    sf.pack(side="top", expand=1, fill="both")
    sf_inner = sf.display_widget(Frame)
    sf_inner.pack(expand=True, fill='both')

    email_label = Label(sf_inner, text='E-mail')
    email_label.grid(row=0, column=0)

    name_label = Label(sf_inner, text='Imię i nazwisko')
    name_label.grid(row=0, column=1)

    points_label = Label(sf_inner, text='Punkty')
    points_label.grid(row=0, column=2)

    add_button = Button(root, text='Dodaj studenta', command=add_student)
    add_button.pack(side="left", padx=10, pady=10)
    add_button = Button(root, text='Wyslij maile', command=mail_all)
    add_button.pack(side="left", padx=10, pady=10)
    add_button = Button(root, text='Wystaw oceny', command=grade_all)
    add_button.pack(side="left", padx=10, pady=10)



    root.mainloop()


init_window()