"""
Módulo transactionObject
------------------------
Responsável por gerenciar a persistência dos dados financeiros em um banco SQLite.
Contém a classe TransactionObject para manipulação de conexões e queries,
além de funções utilitárias para inserir, buscar, atualizar, deletar e gerar relatórios.
"""

import os
import sqlite3 as sql
from collections import defaultdict
import matplotlib.pyplot as plt
from fpdf import FPDF

class TransactionObject:
    """
    Classe TransactionObject
    ------------------------
    Encapsula a conexão com o banco de dados SQLite e fornece métodos
    para executar queries, persistir alterações e recuperar resultados.
    """

    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    database = os.path.join(project_dir, "database", "Finance.db")

    #database = "Finance.db"
    conn = None
    cur = None
    is_connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.is_connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.is_connected = False

    def execute(self, query, params=None):
        if params:
            TransactionObject.cur.execute(query, params)
        else:
            TransactionObject.cur.execute(query)

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        TransactionObject.conn.commit()

def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("""
        CREATE TABLE IF NOT EXISTS Transactions (
            id_transaction INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            amount REAL,
            date TEXT,
            category TEXT
        )
    """)
    trans.persist()
    trans.disconnect()

def insert(type, amount, date, category):
    trans = TransactionObject()
    trans.connect()
    trans.execute(
        "INSERT INTO Transactions (type, amount, date, category) VALUES (?, ?, ?, ?)",
        (type, amount, date, category)
    )
    trans.persist()
    trans.disconnect()

def search(type=None, amount=None, date=None, category=None):
    trans = TransactionObject()
    trans.connect()
    query = "SELECT * FROM Transactions WHERE 1=1"
    params = []

    if type:
        query += " AND type = ?"
        params.append(type)
    if amount:
        query += " AND amount = ?"
        params.append(amount)
    if date:
        query += " AND date = ?"
        params.append(date)
    if category:
        query += " AND category = ?"
        params.append(category)

    trans.execute(query, params)
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def delete(id_transaction):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM Transactions WHERE id_transaction = ?", (id_transaction,))
    trans.persist()
    trans.disconnect()

def update(id_transaction, type, amount, date, category):
    trans = TransactionObject()
    trans.connect()
    trans.execute(
        "UPDATE Transactions SET type=?, amount=?, date=?, category=? WHERE id_transaction=?",
        (type, amount, date, category, id_transaction)
    )
    trans.persist()
    trans.disconnect()

def report(date):
    year = date[:4]
    month = date[5:7]

    con = sql.connect(TransactionObject.database)
    cur = con.cursor()
    def get_data(tipo):
        cur.execute("""
            SELECT category, amount
            FROM Transactions
            WHERE strftime('%Y', date) = ?
            AND strftime('%m', date) = ?
            AND type = ?
        """, (year, month, tipo))
        return cur.fetchall()

    expenses = get_data("Expenses")
    income = get_data("Income")
    con.close()

    def build_chart(data, title, filename):
        resumo = defaultdict(float)
        for cat, val in data:
            resumo[cat] += val
        if not resumo:
            return False
        plt.figure()
        plt.pie(resumo.values(), labels=resumo.keys(), autopct="%1.1f%%")
        plt.title(title)
        plt.savefig(filename)
        plt.close()
        return True

    build_chart(expenses, "Expenses", "expenses.png")
    build_chart(income, "Income", "income.png")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Financial Report - {month}/{year}", ln=True, align="C")
    pdf.ln(10)

    if expenses:
        pdf.cell(0, 10, "Expenses", ln=True)
        pdf.image("expenses.png", x=30, w=150)
        pdf.ln(90)

    if income:
        pdf.cell(0, 10, "Income", ln=True)
        pdf.image("income.png", x=30, w=150)

    project_dir = os.path.dirname(os.path.abspath(__file__))
    pdf.output(os.path.join(project_dir, f"financial_report_{year}_{month}.pdf"))
    


initDB()
