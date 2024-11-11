# -----------pseudo-codice---------------- #
'''
inizio

    definisci classe prodotto_base (classe astratta)
        metodo astratto mostra_info()

    definisci classe prodotto (che estende prodotto_base)
        attributi:
            - nome: nome
            - codice: codice
            - prezzo: prezzo
            - quantita: quantita

        costruttore:
            inizializza nome, codice, prezzo, quantita con gli oggetti appositi

        metodo mostra_info():
            stampa le info del prodotto (nome, codice, prezzo, quantita)

        metodo class method from_list(dati):
            crea un prodotto a partire da una lista di dati

    definisci classe nome:
        attributi:
            - _valore (nome del prodotto)

        proprieta valore:
            restituisce o imposta il nome del prodotto

        metodo modifica():
            se il nome è vuoto, chiedi all'utente di inserire un nome
            se il nome esiste già, chiedi se vuole modificarlo o meno

    definisci classe codice:
        attributi:
            - _codiceprodotto (codice del prodotto)

        proprieta codiceprodotto:
            restituisce o imposta il codice del prodotto

        metodo modifica():
            se il codice esiste, chiedi all'utente se vuole modificarlo

    definisci classe prezzo:
        attributi:
            - _prezzoprodotto (prezzo del prodotto)

        proprieta prezzoprodotto:
            restituisce o imposta il prezzo del prodotto

        metodo modifica():
            se il prezzo è 0, chiedi di inserirne uno nuovo (controlla che sia positivo)
            se il prezzo esiste già, chiedi se vuoi modificarlo e aggiorna

    definisci classe quantita:
        attributi:
            - _quantita_prodotto (quantità del prodotto)

        proprieta quantita_prodotto:
            restituisce o imposta la quantità del prodotto

        metodo modifica():
            se la quantità è 0, chiedi di inserirne una nuova
            se la quantità esiste, chiedi se vuoi modificarla

    definisci classe magazzino:
        attributi:
            - prodotti: un dataframe vuoto (per tenere traccia dei prodotti)

        metodo aggiungi_prodotto(prodotto):
            aggiungi un nuovo prodotto al dataframe con tutte le info

        metodo mostra_magazzino():
            stampa tutte le informazioni dei prodotti nel magazzino

        metodo ricerca_prodotto(nome):
            cerca il prodotto per nome nel dataframe e stampa se trovato

        metodo statico valore_totale(magazzino):
            calcola il valore totale del magazzino (prezzo * quantità)

        metodo gestione_magazzino():
            ciclo infinito che mostra un menu con le opzioni per gestire il magazzino:
                1. aggiungere un nuovo prodotto
                2. modificare il prezzo di un prodotto
                3. modificare la quantità di un prodotto
                4. modificare il nome di un prodotto
                5. modificare il codice di un prodotto
                6. vedere tutto l'inventario
                7. calcolare il valore totale del magazzino
                8. uscire

            se l'utente sceglie "1" (aggiungere un nuovo prodotto):
                - chiedi nome, codice, prezzo, e quantità
                - crea il prodotto e aggiungilo al magazzino

            se l'utente sceglie "2" (modificare il prezzo di un prodotto):
                - cerca il prodotto per nome
                - se esiste, chiedi di inserire il nuovo prezzo

            se l'utente sceglie "3" (modificare la quantità di un prodotto):
                - cerca il prodotto per nome
                - se esiste, chiedi di inserire la nuova quantità

            se l'utente sceglie "4" (modificare il nome di un prodotto):
                - cerca il prodotto per nome
                - se esiste, chiedi di inserire il nuovo nome

            se l'utente sceglie "5" (modificare il codice di un prodotto):
                - cerca il prodotto per nome
                - se esiste, chiedi di inserire il nuovo codice

            se l'utente sceglie "6" (vedere l'inventario):
                - mostra tutti i prodotti nel magazzino

            se l'utente sceglie "7" (calcolare il valore totale):
                - calcola il valore totale del magazzino e stampalo

            se l'utente sceglie "8" (uscire):
                - esci dal programm
'''
# ---------------codice-------------------- #
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

# Classe astratta per Prodotto
class ProdottoBase(ABC):
    @abstractmethod
    def mostra_info(self):
        pass

# Classe Prodotto che estende ProdottoBase
class Prodotto(ProdottoBase):
    def __init__(self, nome="", codice="", prezzo=0.0, quantita=0):
        self.nome = Nome(nome)
        self.codice = Codice(codice)
        self.prezzo = Prezzo(prezzo)
        self.quantita = Quantita(quantita)

    def mostra_info(self):
        print(f"Nome: {self.nome.valore}, Codice: {self.codice.codiceprodotto}, "
              f"Prezzo: {self.prezzo.prezzoprodotto:.2f}, Quantità: {self.quantita.quantita_prodotto}")

    # Metodo class method per creare un Prodotto da una lista di dati
    @classmethod
    def from_list(cls, dati):
        return cls(*dati)

# Classe Nome
class Nome:
    def __init__(self, nomeprodotto):
        self._valore = nomeprodotto

    @property
    def valore(self):
        return self._valore

    @valore.setter
    def valore(self, nomeprodotto):
        self._valore = nomeprodotto

    def modifica(self):
        if not self._valore:
            self._valore = input("Inserisci il nome del prodotto: ")
        else:
            print(f"Nome attuale: {self._valore}")
            modifica = input("Vuoi modificarlo? (s/n): ")
            if modifica.lower() == 's':
                self._valore = input("Inserisci il nuovo nome: ")
                print(f"Nome aggiornato a: {self._valore}")
        input("Premi invio per continuare")

# Classe Codice
class Codice:
    def __init__(self, codiceprodotto):
        self._codiceprodotto = codiceprodotto

    @property
    def codiceprodotto(self):
        return self._codiceprodotto

    @codiceprodotto.setter
    def codiceprodotto(self, codiceprodotto):
        self._codiceprodotto = codiceprodotto

    def modifica(self):
        print(f"Codice attuale: {self._codiceprodotto}")
        modifica = input("Vuoi modificarlo? (s/n): ")
        if modifica.lower() == 's':
            self._codiceprodotto = input("Inserisci il nuovo codice: ")
            print(f"Codice aggiornato a: {self._codiceprodotto}")
        input("Premi invio per continuare")

# Classe Prezzo
class Prezzo:
    def __init__(self, prezzoprodotto):
        self._prezzoprodotto = prezzoprodotto

    @property
    def prezzoprodotto(self):
        return self._prezzoprodotto

    @prezzoprodotto.setter
    def prezzoprodotto(self, prezzoprodotto):
        if prezzoprodotto < 0:
            print("Il prezzo non può essere negativo.")
        else:
            self._prezzoprodotto = prezzoprodotto

    def modifica(self):
        if self._prezzoprodotto == 0:
            while True:
                try:
                    nuovo_prezzo = float(input("Inserisci il prezzo del prodotto: "))
                    if nuovo_prezzo >= 0:
                        self._prezzoprodotto = nuovo_prezzo
                        print(f"Prezzo inserito: {self._prezzoprodotto:.2f}")
                        break
                    else:
                        print("Il prezzo non può essere negativo.")
                except ValueError:
                    print("Prezzo non valido. Inserisci solo numeri.")
        else:
            print(f"Prezzo attuale: {self._prezzoprodotto:.2f}")
            modifica = input("Vuoi modificarlo? (s/n): ")
            if modifica.lower() == 's':
                while True:
                    try:
                        nuovo_prezzo = float(input("Inserisci il nuovo prezzo: "))
                        if nuovo_prezzo >= 0:
                            self._prezzoprodotto = nuovo_prezzo
                            print(f"Prezzo aggiornato a: {self._prezzoprodotto:.2f}")
                            break
                        else:
                            print("Il prezzo non può essere negativo.")
                    except ValueError:
                        print("Prezzo non valido. Inserisci solo numeri.")
        input("Premi invio per continuare")

# Classe Quantita
class Quantita:
    def __init__(self, quantita_prodotto):
        self._quantita_prodotto = quantita_prodotto

    @property
    def quantita_prodotto(self):
        return self._quantita_prodotto

    @quantita_prodotto.setter
    def quantita_prodotto(self, quantita_prodotto):
        if quantita_prodotto < 0:
            print("La quantità non può essere negativa.")
        else:
            self._quantita_prodotto = quantita_prodotto

    def modifica(self):
        if self._quantita_prodotto == 0:
            while True:
                try:
                    nuova_quantita = int(input("Inserisci la quantità del prodotto: "))
                    if nuova_quantita >= 0:
                        self._quantita_prodotto = nuova_quantita
                        print(f"Quantità inserita: {self._quantita_prodotto}")
                        break
                    else:
                        print("La quantità non può essere negativa.")
                except ValueError:
                    print("Quantità non valida. Inserisci solo numeri.")
        else:
            print(f"Quantità attuale: {self._quantita_prodotto}")
            modifica = input("Vuoi modificarla? (s/n): ")
            if modifica.lower() == 's':
                while True:
                    try:
                        nuova_quantita = int(input("Inserisci la nuova quantità: "))
                        if nuova_quantita >= 0:
                            self._quantita_prodotto = nuova_quantita
                            print(f"Quantità aggiornata a: {self._quantita_prodotto}")
                            break
                        else:
                            print("La quantità non può essere negativa.")
                    except ValueError:
                        print("Quantità non valida. Inserisci solo numeri.")
        input("Premi invio per continuare")

# Classe Magazzino
class Magazzino:
    def __init__(self):
        self.prodotti = pd.DataFrame(columns=["Nome", "Codice", "Prezzo", "Quantita"])

    # Metodo per aggiungere un prodotto
    def aggiungi_prodotto(self, prodotto):
        dati_prodotto = [prodotto.nome.valore, prodotto.codice.codiceprodotto, prodotto.prezzo.prezzoprodotto, prodotto.quantita.quantita_prodotto]
        self.prodotti = self.prodotti.append(pd.Series(dati_prodotto, index=self.prodotti.columns), ignore_index=True)

    # Mostra il magazzino
    def mostra_magazzino(self):
        print(self.prodotti)

    # Ricerca prodotto
    def ricerca_prodotto(self, nome):
        risultato = self.prodotti[self.prodotti["Nome"].str.lower() == nome.lower()]
        if not risultato.empty:
            print(risultato)
        else:
            print("Prodotto non esistente.")
        input("Premi invio per continuare")

    # Metodo statico che calcola il valore totale del magazzino
    @staticmethod
    def valore_totale(magazzino):
        return np.sum(magazzino.prodotti["Prezzo"] * magazzino.prodotti["Quantita"])

    # Gestione del magazzino
    def gestione_magazzino(self):
        while True:
            scelta = input("""
Invia 1 se vuoi inserire un nuovo prodotto
Invia 2 se vuoi modificare il prezzo di un prodotto
Invia 3 se vuoi modificare la quantità di un prodotto
Invia 4 se vuoi modificare il nome di un prodotto
Invia 5 se vuoi modificare il codice di un prodotto
Invia 6 se vuoi vedere tutto l'inventario
Invia 7 per calcolare il
