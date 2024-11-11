# 1. @property

class Circonferenza:
    def __init__(self, raggio):
        self._raggio = raggio

    @property
    def raggio(self):
        return self._raggio

    @raggio.setter
    def raggio(self, valore):
        if valore < 0:
            raise ValueError("Il raggio deve essere positivo.")
        self._raggio = valore

    @property
    def area(self):
        return 3.14 * self._raggio ** 2

c = Circonferenza(5)
print(c.area)
c.raggio = 10
print(c.area)

# ----------------------------------------

# 2. @classmethod

class ContoBancario:
    tasso_interesse = 0.05

    def __init__(self, saldo):
        self.saldo = saldo

    @classmethod
    def tasso(cls):
        return cls.tasso_interesse

    def calcola_interesse(self):
        return self.saldo * self.tasso()

conto = ContoBancario(1000)
print(conto.calcola_interesse())

# ----------------------------------------

# 3. @staticmethod

class Matematica:
    
    @staticmethod
    def somma(a, b):
        return a + b

    @staticmethod
    def moltiplicazione(a, b):
        return a * b

print(Matematica.somma(5, 10))
print(Matematica.moltiplicazione(5, 10))

# ----------------------------------------

# 4. @abstractmethod

from abc import ABC, abstractmethod

class Animale(ABC):
    
    @abstractmethod
    def suono(self):
        pass

class Cane(Animale):
    def suono(self):
        return "Bau!"

class Gatto(Animale):
    def suono(self):
        return "Miao!"

cane = Cane()
gatto = Gatto()

print(cane.suono())
print(gatto.suono())

# ----------------------------------------

# 5. Decoratore personalizzato

def decoratore_somma(f):
    def wrapper(a, b):
        risultato = f(a, b)
        print(f"Somma: {risultato}")
        return risultato
    return wrapper

@decoratore_somma
def somma(a, b):
    return a + b

somma(3, 5)

# ----------------------------------------

# Funzioni lambda

sommare = lambda a, b: a + b
moltiplicare = lambda a, b: a * b
print(sommare(3, 4))
print(moltiplicare(3, 4))

# ----------------------------------------

# 1. Somma di due numeri

somma = lambda a, b: a + b
print(somma(3, 5))

# ----------------------------------------

# 2. Moltiplicazione di due numeri

moltiplicazione = lambda a, b: a * b
print(moltiplicazione(4, 6))

# ----------------------------------------

# 3. Verifica se un numero è pari

pari = lambda x: x % 2 == 0
print(pari(10))  # True
print(pari(7))   # False

# ----------------------------------------

# 4. Concatenazione di due stringhe

concatenare = lambda str1, str2: str1 + " " + str2
print(concatenare("Ciao", "Mondo"))

# ----------------------------------------

# 5. Eleva un numero al quadrato

quadrato = lambda x: x ** 2
print(quadrato(9))

