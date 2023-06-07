# Eingabe
#-*- coding:utf-8 -*-

def verdoppler():
    eingabe = input("Bitte geben sie Ihre Zahl ein: ")
#Eingabe
    try:
        str.isdigit(eingabe); #überprüft Eingabe, ob es eine Zahl oder ein String ist
        ausgabe = int(eingabe) * 2
# Ausgabe
        print("Ihre zahl lautet:", ausgabe)
        verdoppler()
    except: verdoppler()

verdoppler()


