# Fitness-Datenanalyse Tool

print("Willkommen zum Fitness-Datenanalyse-Tool!")

# Beispiel-Daten von mehreren Personen
# Format: [Name, Alter, Gewicht, Trainingsstunden/Woche]
personen = [
	["Lorena", 20, 55, 4],
	["Maria", 25, 80, 7],
	["Lea", 30, 68, 2],
	["Ali", 22, 72, 10]
]

# Funktionen
def bmi(gewicht, groesse_m):
	return gewicht / (groesse_m ** 2)

def fitness_level(stunden):
	if stunden >= 10:
		return "Experte"
	elif stunden >= 7:
		return "Profi"
	elif stunden >= 4:
		return "Fortgeschritten"
	else:
		return "Anfänger"

# Datenanalyse
gesamt_stunden = 0
levels = {"Anfänger":0, "Fortgeschritten":0, "Profi":0, "Experte":0}

for person in personen:
	name, alter, gewicht, stunden = person
	level = fitness_level(stunden)
	levels[level] += 1
	gesamt_stunden += stunden
	print(f"{name} → {level}, Trainingsstunden: {stunden}")

durchschnitt = gesamt_stunden / len(personen)
print("\n--- Statistik ---")
print(f"Durchschnittliche Trainingsstunden: {durchschnitt:.1f}")
for level, anzahl in levels.items():
	print(f"{level}: {anzahl} Person(en)")
