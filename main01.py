#!/usr/bin/python3
# -*- coding: utf-8 -*-
# FILE : main01.py
# RUN  : python3 main01.py
#-------------------------------------------------BEGIN file
from tkinter import *
from tkinter import ttk

root = Tk()

fereastra = ttk.Frame(root, padding=10)
fereastra.grid()

ttk.Label(fereastra, text="Salut").grid(column=0, row=0)
ttk.Button(fereastra, text="Inchide", command=root.destroy).grid(
    column=1, row=0)

root.mainloop()
#----------------------------------------------------END file
