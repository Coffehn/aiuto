log_battaglia = []  # Lista che conterrà il log delle azioni della battaglia

# Decoratore per tracciare le azioni
def log_azione(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        risultato = func(self, *args, **kwargs)  # Esegui la funzione originale (es. attacca)
        azione = f"{self.nome} {risultato}"  # Crea una descrizione dell'azione eseguita dal personaggio
        log_battaglia.append(azione)  # Aggiungi l'azione al log
        return risultato
    return wrapper

# Classe astratta Personaggio
class Personaggio(ABC):
    def __init__(self, nome, salute, attacco_base):
        self.nome = nome  # Nome del personaggio
        self.salute = salute  # Salute iniziale del personaggio
        self.attacco_base = attacco_base  # Attacco base del personaggio

    @abstractmethod
    def attacca(self):
        pass  # Ogni sottoclasse deve implementare il proprio metodo di attacco

    def is_alive(self):
        return self.salute > 0  # Verifica se il personaggio è vivo (salute > 0)

# Classe Guerriero
class Guerriero(Personaggio):
    def __init__(self, nome):
        super().__init__(nome, salute=120, attacco_base=15)  # Inizializza il Guerriero con salute e attacco

    @log_azione  # Usa il decoratore per tracciare l'azione
    def attacca(self):
        danno = self.attacco_base + np.random.randint(5, 15)  # Calcola il danno dell'attacco con un valore casuale
        return f"attacca con la spada infliggendo {danno} danni"  # Restituisce una descrizione dell'attacco

# Classe Mago
class Mago(Personaggio):
    def __init__(self, nome):
        super().__init__(nome, salute=80, attacco_base=20)  # Inizializza il Mago con salute e attacco
        self.mana = 100  # Mana iniziale del Mago

    @log_azione  # Usa il decoratore per tracciare l'azione
    def attacca(self):
        danno = self.attacco_base + np.random.randint(10, 20)  # Calcola il danno dell'incantesimo con un valore casuale
        self.mana -= 10  # Riduce il mana del Mago per ogni incantesimo lanciato
        return f"lancia un incantesimo infliggendo {danno} danni, mana rimanente: {self.mana}"  # Restituisce la descrizione dell'azione

# Funzione principale per simulare la battaglia e salvare il log
def battaglia(personaggio1, personaggio2, turni=3):
    for turno in range(1, turni + 1):  # Ciclo per ogni turno della battaglia
        if not (personaggio1.is_alive() and personaggio2.is_alive()):  # Controlla se entrambi i personaggi sono vivi
            break  # Termina la battaglia se uno dei due è morto
        # Ogni personaggio attacca
        personaggio1.attacca()  # Il primo personaggio attacca
        personaggio2.attacca()  # Il secondo personaggio attacca
    
    # Creazione di un DataFrame per il log della battaglia
    df_log = pd.DataFrame(log_battaglia, columns=["Azione"])  # Crea un DataFrame con le azioni nel log

    # Salvataggio del log in un file CSV
    df_log.to_csv("log_battaglia.csv", index=False)  # Esporta il DataFrame in un file CSV senza l'indice
    
    print("\n--- Log della Battaglia ---")  # Stampa del log della battaglia
    print(df_log)  # Mostra il DataFrame con il log
    return df_log  # Restituisce il DataFrame per eventuali elaborazioni successive

# Esecuzione dello script con personaggi
guerriero = Guerriero("Arthas")  # Crea un oggetto Guerriero con il nome "Arthas"
mago = Mago("Gandalf")  # Crea un oggetto Mago con il nome "Gandalf"

# Esecuzione della battaglia e salvataggio del log
battaglia(guerriero, mago, turni=3)  # Simula la battaglia tra il Guerriero e il Mago con 3 turni


# ---------------------------------------- aggiunta recupero mana e difesa speciale

def recupero_mana(self):
    self.mana += 20
    if self.mana > 100:  # Non può superare 100 mana
        self.mana = 100
    return f"recupera 20 mana, mana attuale: {self.mana}"



def difesa_speciale(self):
    return f"usa difesa speciale e non subisce danni questo turno"
# ---------------------------------------- 28f
def calcola_punteggio(giocatori, media_minima=6):
    # Funzione per calcolare la media dei punteggi di un giocatore
    def calcola_media(giocatore):
        return sum(giocatore["punteggi"]) / len(giocatore["punteggi"])

    # Utilizzo di map per calcolare la media dei punteggi per ciascun giocatore
    giocatori_con_media = list(map(lambda giocatore: {**giocatore, "media": calcola_media(giocatore)}, giocatori))

    # Utilizzo di filter per selezionare solo i giocatori con media superiore alla soglia
    giocatori_selezionati = list(filter(lambda giocatore: giocatore["media"] > media_minima, giocatori_con_media))

    # Ordinamento della lista di giocatori selezionati in base alla media, usando lambda
    giocatori_ordinati = sorted(giocatori_selezionati, key=lambda x: x["media"], reverse=True)

    # Restituisci la lista ordinata dei giocatori con la loro media
    return giocatori_ordinati

# Utilizzo
giocatori = [
    {"nome": "A", "punteggi": [8, 7, 6]},
    {"nome": "B", "punteggi": [9, 6, 8]},
    {"nome": "C", "punteggi": [7, 5, 6]}
]

result = calcola_punteggio(giocatori, media_minima=6)
for giocatore in result:
    print(f"{giocatore['nome']} - Media: {giocatore['media']}")
