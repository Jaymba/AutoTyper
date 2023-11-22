from tkinter import *
from tkinter import ttk 

window = Tk()
window.title("AutoTyper")

frm = ttk.Frame(window, padding=10)
frm.grid()


ttk.Button(frm,text="Quit", command=window.destroy).grid(column=3,row=3)


window.mainloop()