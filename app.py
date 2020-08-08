from tkinter import *
from appHs import userOk
from interfaz import interfaz
from appHs import add

logeado = userOk()

if logeado == False:

    window = Tk()

    window.title("autoRedMine")
    window.geometry('350x200')

    lbl_u = Label(window, text="User:",)
    lbl_u.config(font=("Verdana", 12))
    lbl_u.grid(column=1, row=5)

    us = Entry(window, width=15)
    us.grid(column=2, row=5)

    lbl_u = Label(window, text="Password:",)
    lbl_u.config(font=("Verdana", 12))
    lbl_u.grid(column=1, row=6)

    ps = Entry(window, width=15)
    ps.grid(column=2, row=6)



    btn = Button(window, text="Log in", command=add(us.get(), ps.get()))
    btn.grid(column=2, row=7)

    window.mainloop()
else:
    interfaz()
