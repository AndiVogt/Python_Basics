a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))

while True:
    print(f"Was ist die Summe von Variable {a} und {b}")
    nutzereingabe = int(input())
    
    if nutzereingabe == (a+b):
        print("Korrekt Diggi")
        break
    else:
        print("Falsch")
        
print("Das Spiel ist aus, wir gehen nach Haus")
    



