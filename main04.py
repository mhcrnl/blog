#!/usr/bin/python3
#--------------------------------------BEGIN file
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x250')
root.resizable(False, False)
root.title("Checkbox Demo")

agreement = tk.StringVar()

def agreement_changed():
    tk.messagebox.showinfo(title="Rezultat",
                           message=agreement.get())

ttk.Checkbutton(root,
                text="De acord",
                command=agreement_changed,
                variable=agreement,
                onvalue="Acord",
                offvalue="Dezacord").pack()
root.mainloop()
#---------------------------------------END file
