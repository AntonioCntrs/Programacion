import pandas as pd
import matplotlib.pyplot as plt
from database import Database

class Analysis:
    def __init__(self):
        self.db = Database()

    def plot_expenses_by_category(self):
        data = self.db.data
        if not data.empty and 'Monto' in data.columns and pd.api.types.is_numeric_dtype(data['Monto']):
            expenses = data.groupby('Categoría')['Monto'].sum()
            ax = expenses.plot(kind='bar', color='skyblue', edgecolor='black')
            ax.set_title('Gastos por Categoría')
            ax.set_xlabel('Categoría')
            ax.set_ylabel('Monto')
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
            for i in ax.containers:
                ax.bar_label(i, label_type="edge")
            plt.tight_layout()
            plt.show()
        else:
            print("No hay datos numéricos para graficar.")

    def reset_database(self):
        self.db.data = pd.DataFrame(columns=['Fecha', 'Categoría', 'Monto'])
        self.db.save_data()
        print("La base de datos ha sido restablecida.")

    def view_database(self):
        print(self.db.data)