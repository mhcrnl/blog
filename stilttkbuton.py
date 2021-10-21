#!/usr/bin/python3
# -*- coding: utf-8 -*-
# FILE: stilttkbuton.py
# RUN : python3 stilttkbuton.py
#--------------------------------------------------BEGIN file
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x100")
root.title("Stil Ttk Buton")

stil = Style()
stil.configure("W.TButton", font =( 'calibri',
               10, 'bold', 'underline'), foreground='red')

btn1 = Button(root, text="Inchide",
              style='W.TButton',
              command=root.destroy)
btn1.grid(row=0, column=3,padx=100)

btn2 = Button(root, text="Apasă-mă!", command=None)
btn2.grid(row=1, column=3, pady=10, padx=100)

root.mainloop()
#-------------------------------------------------END file
