from functools import partial
from tkinter import *
from tkinter import ttk 
import tkinter as tk
import time
from pynput.keyboard import Controller

keyboard = Controller()

root = Tk()
root.title("AutoTyper")
root.geometry("230x90")


frm = ttk.Frame(root, padding=10)
frm.grid()

for i in range(3):
    frm.grid_columnconfigure(i,weight=1)

for i in range(4):
    frm.grid_rowconfigure(i,weight=0)

ttk.Label(frm,text="Password:").grid(row=0,column=0)

pswd_var = tk.StringVar()
password = ttk.Entry(frm,textvariable=pswd_var).grid(row=0,column=1,columnspan=3)

def SendKeys(ps):
    txt = ps.get()
    root.destroy()
    time.sleep(2)
    keyboard.type(txt)
    


ttk.Button(frm,text="Enter", command=partial(SendKeys, pswd_var)).grid(column=2,row=3,sticky=tk.SE, pady=10)


root.grid_rowconfigure(5, minsize=41)
root.grid_columnconfigure(5, minsize=36)
root.mainloop()