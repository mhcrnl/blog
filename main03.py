#!/usr/bin/python3
#-------------------------------------------------BEGIN file
import tkinter as tk
from tkinter import ttk
# Ferastra root
fereastra = tk.Tk()
fereastra.geometry("300x200")
fereastra.resizable(False, False)
fereastra.title("Fereastra cu button")
# Exit buton
exit_btn = ttk.Button(fereastra, text="Exit",
                      command=fereastra.quit())
exit_btn.pack(ipadx=5, ipady=5, expand=True)
fereastra.mainloop()
#------------------------------------------------END file
