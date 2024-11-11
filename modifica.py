import pandas as pd
from abc import ABC, abstractmethod

# Classe base per lavorare con i file Excel
class ExcelManager(ABC):
    def __init__(self, file_path):
        self.file_path = file_path  # Dove sta il file
        self.df = None  # Questo sarà il nostro DataFrame
        self.load_file()  # Carica il file

    def load_file(self):
        """Carica il file nel DataFrame."""
        try:
            self.df = pd.read_excel(self.file_path)  # Apre il file Excel
        except Exception as e:
            print(f"Errore nel caricare il file: {e}")  # Se c'è un errore, lo dice
    
    @property
    def get_dataframe(self):
        """Restituisce il DataFrame."""
        return self.df

    @abstractmethod
    def modify_file(self):
        """Metodo per modificare il file"""
        pass

    @classmethod
    def merge_dataframes(cls, df1, df2, on_column):
        """Unisce due DataFrame su una colonna"""
        return pd.merge(df1, df2, on=on_column)

    @staticmethod
    def save_file(df, file_path):
        """Salva il DataFrame su un nuovo file Excel"""
        try:
            df.to_excel(file_path, index=False)  # Salva senza gli indici
            print(f"File salvato in {file_path}")
        except Exception as e:
            print(f"Errore nel salvare il file: {e}")

# Classe che fa le modifiche
class ExcelEditor(ExcelManager):
    
    def modify_file(self):
        """Modifica il file come vogliamo"""
        print("Sto modificando il file...")
        
        # Filtra le righe dove 'Età' è maggiore di 30
        self.df = self.df.loc[lambda df: df['Età'] > 30]
        
        # Prende solo le colonne che ci servono
        self.df = self.df[['Nome', 'Età', 'Stipendio']]  # Nome, Età e Stipendio
    
    def apply_custom_function(self, func):
        """Applica una funzione personalizzata al DataFrame"""
        self.df = self.df.apply(func, axis=1)  # Applica la funzione a ogni riga

# Funzione principale
def main():
    # Percorso del file Excel
    file_path = "file.xlsx"
    
    # Crea l'oggetto per modificare il file
    editor = ExcelEditor(file_path)
    
    # Modifica il file
    editor.modify_file()
    
    # Mostra il DataFrame modificato
    print("DataFrame modificato:")
    print(editor.get_dataframe)  # Mostra il DataFrame
    
    # Applica una funzione per aumentare lo stipendio
    editor.apply_custom_function(lambda row: row['Stipendio'] * 1.1 if row['Età'] > 40 else row['Stipendio'])
    
    # Mostra il DataFrame dopo aver applicato la funzione
    print("DataFrame dopo la funzione:")
    print(editor.get_dataframe)
    
    # Salva il file modificato
    editor.save_file(editor.get_dataframe, "file_modificato.xlsx")

if __name__ == "__main__":
    main()