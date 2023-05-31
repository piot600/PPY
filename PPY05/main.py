import tkinter as tk
import tkscrolledframe as sf

students_list = {}
def addstudent():
    addwindow = tk.Toplevel(width=300,height=300)

    name_l =





def mainframe():
    root = tk.Tk()
    root.title("Students list")
    global scrolledframe
    global sfopener

    scrolledframe = sf.ScrolledFrame(root, width=700, height=500)
    scrolledframe.pack(side="right",expand=1,fill="y")
    scf = scrolledframe.display_widget(tk.Frame)
    scf.pack(expand=True, fill="y")

    email_l = tk.Label(scf,text="Email")
    email_l.grid(row=0,column=0)

    name_l = tk.Label(scf, text="Name")
    name_l.grid(row=0, column=1)

    surname_l = tk.Label(scf, text="Surname")
    surname_l.grid(row=0, column=2)

    points_l = tk.Label(scf, text="Points")
    points_l.grid(row=0,column=3)

    grade_l = tk.Label(scf,text="Grade")
    grade_l.grid(row=0,column=4)

    state_l = tk.Label(scf,text="State")
    state_l.grid(row=0,column=5)

    addbutton = tk.Button(root, text="Add Student",command=addstudent)
    addbutton.pack(side="top",padx=15,pady=15)

    addbutton = tk.Button(root, text="Set Grades")
    addbutton.pack(side="top",padx=15,pady=15)

    addbutton = tk.Button(root, text="Send Emails")
    addbutton.pack(side="top", padx=15, pady=15)


    root.mainloop()
mainframe()
