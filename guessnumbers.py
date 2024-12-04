import random

geraden = 0
numbersGuessed = []

# Genereer 3 willekeurige nummers
for i in range(3):
    number = random.randint(0, 30)
    numbersGuessed.append(number)

print(numbersGuessed)

# Laat de gebruiker 5 keer raden
for i in range(5):
    raad = int(input("Raad het nummer: "))  # Zet de invoer om naar een integer
    if raad in numbersGuessed:
        geraden += 1

# Functie voor het bedrag
def bedrag(aantalGeraden):
    bedragen = {0: 0, 1: 10, 2: 30, 3: 60}
    return bedragen.get(aantalGeraden, 0)  # Gebruik .get om 0 te retourneren voor grotere waarden

# Toon het resultaat
print(f"{geraden} numbers correct: {bedrag(geraden)} euros")
