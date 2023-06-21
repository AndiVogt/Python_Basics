

"""
zahl=0
summe = 0
max = 0

while zahl < 5 :
    var = int(input("Bitte Zahl eingeben: "))
    zahl += 1
    summe = summe + var
    if var > max:
        max = var
else: 
    print("Summe ist gleich: ", summe/5)
    print("Maximum ist: ",max)
"""    

"""
#While und for Schleifen
for i in range(1, 11,3):              #1*1 abarbeiten 3. Kommastelle rechnet mit Schrittfolge
    for j in range(1, 11,3):
        print(f"{i}*{j}={i*j}")
"""
"""

menge = ["rot","grün","blau"]
for i in menge:
    print(i)


"""


"""
for i in range(10):
    print(i)
"""

"""
a = 0

while a < 20:
    a+=1
    if a%2 ==1:
        
        continue
    else:
        print(a)
    
"""



"""
zahl = 3
versuch = 0 
while zahl != versuch:
    versuch = int(input("Zahl raten:"))
    if versuch == 0:
        break
else: 
    print("richtig")
"""




"""a = 0
while a>1:
    print(a)
    a += 1
    """


"""
zahl = int(input("PUTIN your number(max.100):  "))
if (1 <= zahl <= 100):
    if (zahl % 2) == 0:
        print("Sie Zahl ist gerade")
    else: 
        print("Die Zahl ist ungerade")
else: 
    print("Zahl liegt nicht zwischen 1 und 100")
"""
"""
a = 2
#structural pattern matching(abfragen, welchen wert a hat)
match a:
    case 0:
        print("a ist 0")
    case 1:
        print("a ist 1")
    case 2:
        print("a ist 2")

"""

"""
if a>0:
    vorzeichen = "positiv"
else:
    vorzeichen = "negativ"
print(vorzeichen)

vorzeichen ="positiv" if a>0 else "negativ"
print(vorzeichen)"""

"""
if b>0:
    if a>0 :
        print("beide größer 0")
    else:
        print("b>0 und a <=0")
else:
    print("b <= 0")
    
if b>0 and a>0:
    print("beide größer 0")
elif b>0 and a<0:
    print("b>0 and a<0")
else:
    print("b <= 0")
    """