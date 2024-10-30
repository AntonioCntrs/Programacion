import tkinter as tk
from tkinter import ttk
from database import Database
from analysis import Analysis

class FinanceApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("Gestión de Finanzas Personales")

        self.create_widgets()

    def create_widgets(self):
        self.label_fecha = ttk.Label(self.root, text="Fecha (YYYY-MM-DD):")
        self.label_fecha.grid(row=0, column=0)
        self.entry_fecha = ttk.Entry(self.root)
        self.entry_fecha.grid(row=0, column=1)

        self.label_categoria = ttk.Label(self.root, text="Categoría:")
        self.label_categoria.grid(row=1, column=0)
        self.entry_categoria = ttk.Entry(self.root)
        self.entry_categoria.grid(row=1, column=1)

        self.label_monto = ttk.Label(self.root, text="Monto:")
        self.label_monto.grid(row=2, column=0)
        self.entry_monto = ttk.Entry(self.root)
        self.entry_monto.grid(row=2, column=1)

        self.button_add = ttk.Button(self.root, text="Agregar Transacción", command=self.add_transaction)
        self.button_add.grid(row=3, column=0, columnspan=2)

        # Botón para mostrar análisis
        self.button_analysis = tk.Button(self.root, text="Mostrar Análisis", command=self.plot_expenses_by_category)
        self.button_analysis.grid(row=4, column=0, columnspan=2)

        # Botón para restablecer la base de datos
        self.button_reset = tk.Button(self.root, text="Restablecer Base de Datos", command=self.reset_database)
        self.button_reset.grid(row=5, column=0, columnspan=2)

        # Botón para visualizar la base de datos
        self.button_view = tk.Button(self.root, text="Visualizar Base de Datos", command=self.view_database)
        self.button_view.grid(row=6, column=0, columnspan=2)

    def add_transaction(self):
        try:
            fecha = self.entry_fecha.get()
            categoria = self.entry_categoria.get()
            monto = float(self.entry_monto.get())
            self.db.add_transaction(fecha, categoria, monto)
            self.entry_fecha.delete(0, tk.END)
            self.entry_categoria.delete(0, tk.END)
            self.entry_monto.delete(0, tk.END)
        except ValueError:
            print("Error: Asegúrate de que el monto sea un número y la fecha esté en el formato correcto.")

    def plot_expenses_by_category(self):
        analysis = Analysis()
        analysis.plot_expenses_by_category()

    def reset_database(self):
        analysis = Analysis()
        analysis.reset_database()
        self.db.load_data()  # Recargar la base de datos después de restablecerla

    def view_database(self):
        data_window = tk.Toplevel(self.root)
        data_window.title("Base de Datos")

        tree = ttk.Treeview(data_window)
        
        # Definir las columnas
        tree["columns"] = ("Fecha", "Categoría", "Monto")
        
        # Formatear las columnas
        tree.column("#0", width=0, stretch=tk.NO)  # Columna fantasma
        tree.column("Fecha", anchor=tk.W, width=100)
        tree.column("Categoría", anchor=tk.W, width=100)
        tree.column("Monto", anchor=tk.W, width=100)

        # Encabezados de las columnas
        tree.heading("#0", text="", anchor=tk.W)  # Columna fantasma
        tree.heading("Fecha", text="Fecha", anchor=tk.W)
        tree.heading("Categoría", text="Categoría", anchor=tk.W)
        tree.heading("Monto", text="Monto", anchor=tk.W)

        # Insertar datos en el Treeview
        for index, row in self.db.data.iterrows():
            tree.insert("", index, values=(row["Fecha"], row["Categoría"], row["Monto"]))

        tree.pack(expand=True, fill='both')