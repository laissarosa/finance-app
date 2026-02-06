"""
Módulo Connecting
-----------------
Responsável por integrar a interface gráfica (FinanceAppGui) com
a lógica de persistência (TransactionObject). Define os botões
e suas ações: adicionar, buscar, atualizar, deletar e gerar relatórios.
"""

from gui.FinanceAppGui import FinanceAppGui
from aplication import TransactionObject as core
from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from collections import defaultdict
import sqlite3

class Connecting(FinanceAppGui):
    """
    Classe Connecting
    -----------------
    Herda de FinanceAppGui e adiciona funcionalidades de interação
    com o banco de dados. Permite ao usuário manipular transações
    e visualizar relatórios diretamente na interface.
    """

    def __init__(self):
        super().__init__()
        self._create_button("Generate Report", self.generate_report, 6)
        self._create_button("Search", self.search_transaction, 7)
        self._create_button("Add", self.add_transaction, 8)
        self._create_button("Update", self.update_transaction, 9)
        self._create_button("Delete", self.delete_transaction, 10)
        self._create_button("Close", self.window.destroy, 11)

    def _create_button(self, text, command, row):
        Button(self.window, text=text, command=command).grid(
            row=row, column=0, columnspan=2, sticky="WE", padx=self.x_pad, pady=self.y_pad
        )

    def generate_report(self):
        date = self.date_entry.get()
        if not date:
            return

        core.report(date)

        self.show_expense_chart(date)

    def show_expense_chart(self, date):
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        year = date[:4]
        month = date[5:7]

        con = sqlite3.connect(core.TransactionObject.database)
        cur = con.cursor()
        cur.execute("""
            SELECT category, amount
            FROM Transactions
            WHERE strftime('%Y', date) = ?
            AND strftime('%m', date) = ?
            AND type = 'Expenses'
        """, (year, month))
        rows = cur.fetchall()
        con.close()

        resumo = defaultdict(float)
        for cat, val in rows:
            resumo[cat] += val

        if not resumo:
            Label(self.graph_frame, text="Nenhum gasto encontrado para este período.").pack()
            return

        # Cria o gráfico de pizza
        fig = Figure(figsize=(4, 4))
        ax = fig.add_subplot(111)
        ax.pie(resumo.values(), labels=resumo.keys(), autopct="%1.1f%%")
        ax.set_title("Expenses by Category")

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def search_transaction(self):
        self.list_transactions.delete(0, END)
        rows = core.search(
            self.type.get(),
            self.amount.get(),
            self.date_entry.get(),
            self.category.get()
        )
        for row in rows:
            self.list_transactions.insert(END, row)

    def add_transaction(self):
        core.insert(
            self.type.get(),
            self.amount.get(),
            self.date_entry.get(),
            self.category.get()
        )
        self.search_transaction()

    def update_transaction(self):
        if not self.list_transactions.curselection():
            messagebox.showwarning("Warning", "Select a transaction to update")
            return

        selected = self.list_transactions.get(self.list_transactions.curselection())
        core.update(
            selected[0],
            self.type.get(),
            self.amount.get(),
            self.date_entry.get(),
            self.category.get()
        )
        self.search_transaction()

    def delete_transaction(self):
        selected = self.list_transactions.get(self.list_transactions.curselection())
        core.delete(selected[0])
        self.search_transaction()

if __name__ == "__main__":
    app = Connecting()
    app.run()