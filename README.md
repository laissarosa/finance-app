# 💰 Finance App

## 📌 Sobre o projeto
O **Finance App** é uma aplicação desktop desenvolvida em **Python** para controle financeiro pessoal. Ele permite ao usuário registrar transações, consultar dados, atualizar informações, deletar registros e gerar relatórios financeiros completos em PDF com gráficos de despesas e receitas.

## 🚀 Funcionalidades
- **Cadastro de transações**: insira tipo (Receita/Despesa), valor, data e categoria.  
- **Busca avançada**: filtre transações por tipo, valor, data ou categoria.  
- **Atualização e exclusão**: edite ou remova transações existentes.  
- **Relatórios financeiros**: gere relatórios mensais em PDF com gráficos de pizza para despesas e receitas.  
- **Visualização gráfica**: veja a distribuição de gastos por categoria diretamente na interface.  
- **Interface amigável**: construída com **Tkinter**, simples e intuitiva.  

## 🛠️ Tecnologias utilizadas
- **Python 3.13**  
- **SQLite3** → banco de dados leve e embutido, sem necessidade de instalação externa.  
- **Tkinter** → interface gráfica.  
- **Matplotlib** → geração de gráficos.  
- **FPDF** → criação de relatórios em PDF.  
- **Tkcalendar** → seleção de datas na interface.  

## 📂 Estrutura do projeto
finance_app/
│
├── gui/
│   └── FinanceAppGui.py        # Interface gráfica
│
├── aplication/
│   ├── Connecting.py           # Integra GUI e lógica
│   └── TransactionObject.py    # Persistência e operações no banco
│
└── database/
    └── Finance.db              # Banco de dados SQLite

## ⚙️ Como executar
1. Clone o repositório:
   git clone https://github.com/laissa-rosa/finance-app.git
2. Instale as dependências:
   pip install -r requirements.txt
3. Execute a aplicação:
   python -m aplication.Connecting

# 💰 Finance App

## 📌 About the project
**Finance App** is a desktop application developed in **Python** for personal financial management. It allows users to record transactions, search data, update information, delete records, and generate complete financial reports in PDF format with expense and income charts.

## 🚀 Features
- **Transaction registration**: add type (Income/Expense), amount, date, and category.  
- **Advanced search**: filter transactions by type, amount, date, or category.  
- **Update and delete**: edit or remove existing transactions.  
- **Financial reports**: generate monthly PDF reports with pie charts for expenses and income.  
- **Graphical visualization**: view expense distribution by category directly in the interface.  
- **User-friendly interface**: built with **Tkinter**, simple and intuitive.  

## 🛠️ Technologies used
- **Python 3.13**  
- **SQLite3** → lightweight embedded database, no external installation required.  
- **Tkinter** → graphical user interface.  
- **Matplotlib** → chart generation.  
- **FPDF** → PDF report creation.  
- **Tkcalendar** → date selection in the interface.  

## 📂 Project structure
finance_app/
│
├── gui/
│   └── FinanceAppGui.py        # Graphical interface
│
├── aplication/
│   ├── Connecting.py           # Integrates GUI and logic
│   └── TransactionObject.py    # Persistence and database operations
│
└── database/
    └── Finance.db              # SQLite database

## ⚙️ How to run
1. Clone the repository:
   git clone https://github.com/laissa-rosa/finance-app.git
2. Install dependencies:
   pip install -r requirements.txt
3. Run the application:
   python -m aplication.Connecting
