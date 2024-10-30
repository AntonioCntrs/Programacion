import pandas as pd  # Importa la librería pandas para el manejo de datos

class Database:
    def __init__(self, filename='finanzas.csv'):
        self.filename = filename  # Nombre del archivo CSV donde se almacenan los datos
        self.load_data()  # Carga los datos al inicializar la clase

    def load_data(self):
        try:
            self.data = pd.read_csv(self.filename)  # Intenta cargar los datos desde el archivo CSV
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=['Fecha', 'Categoría', 'Monto'])  # Si no existe el archivo, crea un DataFrame vacío

    def save_data(self):
        self.data.to_csv(self.filename, index=False)  # Guarda los datos en el archivo CSV

    def add_transaction(self, fecha, categoria, monto):
        new_transaction = pd.DataFrame({'Fecha': [fecha], 'Categoría': [categoria], 'Monto': [monto]})  # Crea un DataFrame con la nueva transacción
        if not new_transaction.empty:
            self.data = pd.concat([self.data, new_transaction], ignore_index=True)  # Añade la nueva transacción al DataFrame existente
            self.save_data()  # Guarda los datos actualizados