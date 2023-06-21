# String
# Kette von Zeichen
# iterierbar, verknüpfbar
string = "Alex ist der coolste BE"

# Integer
# Zahl 
# mathematische Operatoren verwendbar
integer = 105

# Fließkommazahl
float_number = 23.5

# Nichts, Null, Void
# Platzhalter
empty = None

# Boolean, Wahrheitswerte
boolean1 = False
boolean2 = True



# Listen
# iterierbar
# sortiert
# zugriff auf einzelne Elemente mit listen_name[index]
# Index beginnt bei 0
liste = [1, 2, "Alex", 4, 5]
# ergänzen von Listeneinträgen 
liste.append(6)


# Dictionary
# unsortiert
# effizienter, iterierbar, schneller
dictionary = {
    "Artikelname": "Stahlblech",
    "Materialnummer": 87654321,
    "Menge": 5,
}
# ergänzen von Einträgen
dictionary["Preis"] = 23.5

alter = input("Gib dein Alter ein ")
try:
    alter = int(alter)
    print("du bist ", alter, "Jahre alt")
except:
    print("Gib eine ganze Zahl ein")

