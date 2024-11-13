#-------------------PSEUDO-CODICE---------------------#
#                   idea iniziale                     #
'''
1. inizializzare i personaggi del party (nome, hp, mana, attacco, difesa, precisione, cristalli)
2. inizializzare il nemico (nome, hp, attacco, difesa, abilità speciali)

3. inizio della battaglia:
   mentre (tutti i personaggi nel party sono vivi e il nemico è vivo):
       1. per ogni personaggio nel party:
            se il personaggio è vivo allora:
                mostra lo stato (hp, mana, cristalli)
                scegli un'azione per il personaggio:
                    1. se l'azione è "attacco" allora:
                        - calcola un numero casuale da 1 a 100
                        - se il numero casuale è minore o uguale alla precisione del personaggio:
                            calcola danno = attacco del personaggio - difesa del nemico
                            se danno < 0 allora danno = 0
                            riduci l'hp del nemico di danno
                        altrimenti: il personaggio ha mancato l'attacco
                    2. se l'azione è "curare" allora:
                        - se il personaggio ha abbastanza mana o cristalli:
                            scegli un altro personaggio del party da curare (oppure se stesso)
                            aumenta hp del bersaglio
                    3. se l'azione è "potenziamento" allora:
                        - se il personaggio ha abbastanza risorse (cristalli o mana):
                            aumenta la precisione, la difesa o altre statistiche
                    4. se l'azione è "azioni speciali" allora:
                        - se il personaggio ha cristalli o mana:
                            esegui un'azione speciale (double shot, snipe shot, ecc.)

       2. se il nemico è vivo allora:
            sceglie un'azione:w
                1. se l'abilità scelta è "rage":
                    - aumenta il danno del nemico per il prossimo attacco
                2. se l'abilità scelta è "curse":
                    - sceglie un personaggio del party come bersaglio per il curse
                    - infligge danni nel tempo al bersaglio per i prossimi turni
                3. se l'abilità scelta è "sorrow":
                    - aumenta la difesa del nemico
                4. se l'abilità scelta è "this is the end":
                    - danneggia tutti i membri del party (danno ad area)

       3. applica gli effetti di curse se il nemico ha attivato curse

       4. verifica se qualcuno è morto:
            se un personaggio ha hp <= 0:
                il personaggio è morto
            se il nemico ha hp <= 0:
                il nemico è sconfitto
            se tutti i membri del party sono morti:
                la battaglia è persa

       5. incrementa il turno (avanza al prossimo round)
   
4. fine della battaglia:
   se il nemico è morto:
       stampa "hai vinto! il nemico è stato sconfitto!"
   se tutti i membri del party sono morti:
       stampa "hai perso! tutti i membri del party sono stati sconfitti."

descrizione:

    inizializzazione: si crea il party di personaggi e il nemico con tutte le proprietà necessarie (hp, attacco, difesa, etc.).

    ciclo della battaglia: la battaglia continua finché ci sono personaggi vivi nel party e il nemico è vivo. ogni round:
        ogni personaggio sceglie un'azione (attacco, cura, potenziamento, azioni speciali) in base alle risorse disponibili.
        il nemico sceglie un'azione tra le sue abilità speciali (rage, curse, sorrow, this is the end) e applica gli effetti del turno.

    azioni e abilità speciali:
        attacco: i personaggi calcolano la probabilità di colpire, infliggendo danno al nemico.
        curare: un personaggio può curare se stesso o un altro personaggio, aumentando i suoi hp.
        potenziamento: può potenziare le proprie statistiche (es. precisione, difesa).
        azioni speciali: usano risorse (mana o cristalli) per eseguire attacchi potenti come double shot o snipe shot.
        abilità del nemico: il nemico ha diverse abilità speciali che possono aumentare il proprio attacco, infliggere danni nel tempo (curse), o danneggiare il party con un attacco ad area.

    verifica della vittoria o sconfitta: la battaglia termina quando il nemico o tutti i membri del party sono morti. in caso di vittoria, il messaggio sarà che il nemico è stato sconfitto, in caso di sconfitta, tutti i membri del party sono morti.

comportamento della battaglia

    il ciclo della battaglia è costituito da turni alternati tra il party e il nemico.
    ogni turno, il party agisce prima e poi il nemico sceglie una delle sue azioni tramite randomizer.
    le azioni dei personaggi e del nemico dipendono dalle risorse disponibili (mana, cristalli, ecc.) e dalle condizioni attuali della battaglia.
    il sistema di cura, potenziamento e danno.
    '''
#-----------------------CODICE------------------------#
#                     definitivo                      #
import random

# Decoratore per tracciare le azioni
def log_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Azioni eseguite: {result}")
        return result
    return wrapper

# Definizione dei personaggi
class Character:
    def __init__(self, name, hp, mana, attack, defense, precision, crystals=0):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.precision = precision
        self.crystals = crystals

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} subisce {damage} danni! HP restanti: {self.hp}")

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} guarisce {amount} HP! HP attuali: {self.hp}")

    def regenerate_mana(self, amount):
        self.mana += amount
        print(f"{self.name} ha recuperato {amount} mana! Mana attuale: {self.mana}")

    def regenerate_crystals(self, amount):
        self.crystals += amount
        print(f"{self.name} ha guadagnato {amount} cristalli! Cristalli attuali: {self.crystals}")

    def attack_enemy(self, enemy):
        hit_chance = random.randint(1, 100)
        if hit_chance <= self.precision:
            damage = self.attack - enemy.defense
            if damage < 0:
                damage = 0
            print(f"{self.name} attacca con successo, infliggendo {damage} danni!")
            enemy.take_damage(damage)
            return damage
        else:
            print(f"{self.name} ha mancato l'attacco!")
            return 0

class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.rage_damage = 0  #Rage
        self.sorrow_defense = 0  #Sorrow
        self.curse_turns = 0  # Conta i turni di Curse
        self.curse_target = None  # Personaggio su cui applicare Curse

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        """Metodo per ridurre l'HP del nemico quando subisce danni."""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} subisce {damage} danni! HP restanti: {self.hp}")

    def attack_player(self, party):
        target = random.choice(party)
        crit_chance = random.randint(1, 100)
        is_critical = crit_chance <= 10  # 10% possibilità critico
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0

        if is_critical:
            damage *= 2  # critico danno x2
            print(f"Darlene esegue un colpo critico!")
        else:
            print(f"Darlene {self.name} attacca {target.name}, infliggendo {damage} danni!")

        target.take_damage(damage)

    def choose_action(self, party):
        action = random.choice(['Rage', 'Curse', 'Sorrow', 'This is the End'])

        if action == 'Rage':
            self.rage_attack()

        elif action == 'Curse' and self.curse_turns == 0:
            self.curse(party)

        elif action == 'Sorrow':
            self.sorrow()

        elif action == 'This is the End':
            self.this_is_the_end(party)

    def rage_attack(self):
        self.attack += 1  # Aumenta il danno di 1 ogni volta che viene usato
        print(f"{self.name} ha usato Rage! Il suo danno è aumentato di 1.")

    def curse(self, party):
        self.curse_turns = 4  # Imposta 4 turni di Curse
        self.curse_target = random.choice(party)  # Sceglie un bersaglio casuale
        print(f"{self.name} ha lanciato Curse su {self.curse_target.name}!")

    def sorrow(self):
        self.defense += 1  # Aumenta la difesa ogni volta che viene usata
        print(f"{self.name} ha usato Sorrow! La sua difesa è aumentata di 1.")

    def this_is_the_end(self, party):
        print(f"{self.name} ha usato This is the End! Non puoi più tirarti indietro!")
        for character in party:
            damage = 10
            character.take_damage(damage)
            print(f"{self.name} infligge 10 danni {character.name} non può più scappare dal suo destino!")

    def apply_curse(self):
        if self.curse_turns > 0:
            self.curse_turns -= 1
            self.curse_target.take_damage(5)
            print(f"{self.name} Una maledizione viene inflitta su {self.curse_target.name}!")
            if self.curse_turns == 0:
                print(f"{self.name} La maledizione sembra essersi sciolta...")

# Funzione per scegliere un'azione per ogni personaggio
def choose_action(character, party, enemy):
    if not character.is_alive():
        print(f"{character.name} Non risponde... Salta il turno")
        return 0  # Personaggio morto, salta il turno

    print(f"\nTurno di {character.name}:")
    print(f"HP: {character.hp}, Mana: {character.mana}, Cristalli: {character.crystals}")
    
    # Azioni per il Ranger
    if character.name == 'LutLut':
        action = input("Scegli un'azione:\n1- Concentrate (Aumenta la precisione, costa 10 cristalli)\n2- Double Shot (10 danni, costa 1 cristallo e rigenera 5 cristalli)\n3- Snipe Shot (50 danni, bassa probabilità, costa 20 cristalli)\n")
        if action == '1' and character.crystals >= 10:  # Concentrate
            character.crystals -= 10
            character.precision += 10  # Aumenta la precisione
            print(f"{character.name} ha usato Concentrate! La precisione è aumentata.")
            return 0  # Non infligge danno
        elif action == '2' and character.crystals >= 1:  # Double Shot
            character.crystals -= 1
            damage = 10
            character.regenerate_crystals(5)  # Rigenera 5 cristalli
            print(f"{character.name} ha usato Double Shot, infliggendo {damage} danni!")
            enemy.take_damage(damage)
            return damage
        elif action == '3' and character.crystals >= 20:  # Snipe Shot
            character.crystals -= 20
            hit_chance = random.randint(1, 100)
            if hit_chance <= 30:  # 30% di probabilità di colpire
                damage = 50
                print(f"{character.name} ha colpito con Snipe Shot infliggendo {damage} danni!")
                enemy.take_damage(damage)
                return damage
            else:
                print(f"{character.name} ha mancato il Snipe Shot!")
                return 0
        else:
            print("Non hai abbastanza cristalli per fare questa azione!")
            return 0

    # Azioni per il Mago
    if character.name == 'Sarvente':
        action = input("Scegli un'azione:\n1- Mana Regen (Recupera 10 mana)\n2- Prayers of Protection (Protegge il party, costa 50 mana)\n3- Healing Wave (Cura 25 HP)\n")
        if action == '1' and character.mana >= 10:
            character.regenerate_mana(10)
            return 0  # Non infligge danno
        elif action == '2' and character.mana >= 50:  # Prayers of Protection
            character.mana -= 50
            print(f"{character.name} ha usato Prayers of Protection, il party viene coperto da un velo protettivo!")
            return 0  # Non infligge danno
        elif action == '3' and character.mana >= 25:  # Healing Wave
            target_name = input("Chi vuoi curare? (1: Sarvente, 2: LutLut, 3: Burn): ")
            target = party[int(target_name) - 1]  # Seleziona il personaggio da curare
            target.heal(25)
            print(f"{character.name} ha curato {target.name} di 25 HP!")
            return 0  # Non infligge danno
        else:
            print("Non hai abbastanza mana per fare questa azione!")
            return 0

    # Azioni per il Guerriero
    if character.name == 'Burn':
        action = input("Scegli un'azione:\n1- Power Strike (30 danni, costa 20 mana)\n2- Last Resistance (Aumenta la difesa, costa 10 mana)\n3- Taunt (Provoca il nemico, costa 10 cristalli)\n")
        if action == '1' and character.mana >= 20:  # Power Strike
            character.mana -= 20
            damage = 30
            print(f"{character.name} ha usato Power Strike, infliggendo {damage} danni!")
            enemy.take_damage(damage)
            return damage
        elif action == '2' and character.mana >= 10:  # Shield Block
            character.mana -= 10
            character.defense += 5  # Aumenta la difesa
            print(f"{character.name} ha usato Last Resistance, aumentando la difesa di 5!")
            return 0  # Non infligge danno
        elif action == '3' and character.crystals >= 10:  # Taunt
            character.crystals -= 10
            # Il nemico sarà più incline a colpire il Guerriero nei turni successivi
            print(f"{character.name} ha usato Taunt! Darlene è provocata e attaccherà più probabilmente {character.name}!")
            return 0  # Non infligge danno
        else:
            print("Non hai abbastanza risorse per fare questa azione!")
            return 0

# Funzione di battaglia (loop di battaglia)
def battle(party, enemy):
    round_counter = 1
    while all([character.is_alive() for character in party]) and enemy.is_alive():
        print(f"\n--- Round {round_counter} ---")
        
        # Ogni personaggio sceglie la sua azione
        for character in party:
            choose_action(character, party, enemy)

        # Il nemico sceglie la sua azione
        if enemy.is_alive():
            enemy.choose_action(party)
            enemy.apply_curse()  # Applica i danni del "Curse" se necessario

        # Controlla se la battaglia è finita
        if not enemy.is_alive():
            print(f"\n{enemy.name} la strega è stata sconfitta!")
            break
        elif not any(character.is_alive() for character in party):
            print("\nTutti i membri del party sono stati sconfitti!")
            break

        round_counter += 1

# Creazione dei personaggi e nemico
ranger = Character(name="LutLut", hp=100, mana=50, attack=15, defense=5, precision=80, crystals=100)
mago = Character(name="Sarvente", hp=80, mana=100, attack=10, defense=3, precision=70, crystals=100)
guerriero = Character(name="Burn", hp=150, mana=50, attack=20, defense=10, precision=60, crystals=100)

party = [ranger, mago, guerriero]

# Creazione del nemico
enemy = Enemy(name="Darlene", hp=200, attack=25, defense=8)

# Inizio della battaglia
battle(party, enemy)
