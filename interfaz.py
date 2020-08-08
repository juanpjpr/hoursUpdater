
from tkinter import *
from appHs import lectura
from programin import guardarHoras
from appHs import last


def interfaz():
    window = Tk()

    window.title("autoRedMine")
    window.geometry('350x200')
    params = lectura()


    def update():
        guardarHoras(params[0], params[1], isue.get(), hs.get(), coment.get())

    # user

  
    u = StringVar()
    u.set(params[0])
    lbl_u = Label(window, textvariable=u)
    lbl_u.config(font=("Verdana", 24))
    lbl_u.grid(column=1, row=1)
    # issue

    i = StringVar()
    i.set(params[2])
    lbl_i = Label(window, text="Issue #",)
    lbl_i.config(font=("Verdana", 16))
    lbl_i.grid(column=1, row=2)

    isue = Entry(window, width=10, textvariable=i)
    isue.grid(column=2, row=2)
    # seteo la hs


    lbl_hs = Label(window, text="Hs:",)
    lbl_hs.config(font=("Verdana", 16))
    lbl_hs.grid(column=1, row=3)

    h = IntVar()
    h.set(params[3])
    hs = Spinbox(window, from_=0, to=24, textvariable=h, width=8)
    hs.grid(column=2, row=3)
    # seteo comentario
 
    c = StringVar()
    c.set(params[4])
    lbl_coment = Label(window, text="Comentarios:")
    lbl_coment.config(font=("Verdana", 16))
    lbl_coment.grid(column=1, row=4)

    coment = Entry(window, width=15, textvariable=c)
    coment.grid(column=2, row=4)

    # button
    btn = Button(window, text="UPDATE", command=update)
    btn.grid(column=2, row=7)
    stats = last()
    lbl_last = Label(window, text="Last Update:"+stats[0] + " - "+stats[1])
    lbl_last.grid(column=1, row=10)
    coment.focus()

    window.mainloop()
