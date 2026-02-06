"""
Módulo FinanceAppGui
--------------------
Responsável por construir a interface gráfica principal da aplicação
de controle financeiro. Utiliza Tkinter e tkcalendar para entrada de dados.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry

class FinanceAppGui:
    """
    Classe FinanceAppGui
    --------------------
    Cria a janela principal da aplicação, com campos de entrada
    para tipo de transação, valor, data e categoria, além de uma
    lista de transações e espaço para gráficos.
    """

    def __init__(self):
        self.x_pad = 15
        self.y_pad = 12
        self.width_entry = 40

        self.window = tk.Tk()
        self.window.title("Financial Control")
        Label(self.window, text="Let's get your finances organized today!").grid(row=0, column=0, columnspan=2, pady=10)

        self.type = tk.StringVar()
        self.amount = tk.DoubleVar()
        self.category = tk.StringVar()

        Label(self.window, text="Type").grid(row=1, column=0)
        ttk.Combobox(self.window, textvariable=self.type, values=["Income", "Expenses"], width=self.width_entry).grid(row=1, column=1)

        Label(self.window, text="Amount").grid(row=2, column=0)
        Entry(self.window, textvariable=self.amount, width=self.width_entry).grid(row=2, column=1)

        Label(self.window, text="Date").grid(row=3, column=0)
        self.date_entry = DateEntry(
            self.window,
            width=self.width_entry,
            background="white",
            foreground="black",
            date_pattern="yyyy-mm-dd"
        )
        self.date_entry.grid(row=3, column=1)

        Label(self.window, text="Category").grid(row=5, column=0)
        ttk.Combobox(
            self.window,
            textvariable=self.category,
            values=["Food","Rent","Bills","Salary","Pharmacy","Clothing","Transportation","Leisure","Travel","Credit Card","Others"],
            width=self.width_entry,
            state="readonly"
        ).grid(row=5, column=1)

        self.list_transactions = Listbox(self.window, width=90)
        self.list_transactions.grid(row=1, column=2, rowspan=10, sticky="NS")

        scrollbar = Scrollbar(self.window)
        scrollbar.grid(row=1, column=3, rowspan=10, sticky="NS")
        self.list_transactions.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.list_transactions.yview)

        self.graph_frame = Frame(self.window)
        self.graph_frame.grid(row=1, column=4, rowspan=10, padx=10)

    def run(self):
        self.window.mainloop()