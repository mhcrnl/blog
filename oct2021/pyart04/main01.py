#!/usr/bin/python3
# -*- coding: utf-8 -*-
#--------------------------------------------------------------
# FILE: main01.py
# RUN : python3 main01.py
#--------------------------------------------------------------
from tkinter import *
#import tkinter as tk
from tkinter import ttk
#-------------------------------------------------------------
class Aplicatie(ttk.Frame):
    """ Documentatia clasei apare aici"""
    
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.text_ent = ttk.Entry()
        self.text_ent.pack()

        # Crearea variabilei
        self.continut = tk.StringVar()
        # Adaugarea unei valori
        self.continut.set("Acesta este textul continut.")
        # In vidgetul text_ent adaugam conținutul vriabilei
        self.text_ent["textvariable"] = self.continut

        # Definim o apelare pentru afișarea continut
        self.text_ent.bind('<Key-Return>', self.afiseaza_continut)

    def afiseaza_continut(self, event):
        """ Documentatia metodei apare aici."""
        
        print("Afiseaza continutul: ", self.continut.get())

root = Tk()
aplicatia_mea = Aplicatie(root)
aplicatia_mea.master.title("Aplicatia mea!")
aplicatia_mea.master.geometry("600x400")
aplicatia_mea.mainloop()

#---------------------------------------------------------END
