Entwickeln Sie einen Taschenrechner, der einfache mathematische Operationen ausführen kann. Der Taschenrechner sollte:

1. Den Benutzer auffordern, zwei Zahlen und eine der folgenden Operationen einzugeben: addieren, subtrahieren, multiplizieren, dividieren.
2. Die entsprechende Operation durchführen und das Ergebnis ausgeben.
3. Eine Möglichkeit bieten, eine weitere Berechnung durchzuführen oder das Programm zu beenden.
4. Bei ungültigen Eingaben (z. B. Division durch Null) sollte das Programm eine Fehlermeldung ausgeben und den Benutzer auffordern, seine Eingabe zu korrigieren.

## Operationsfunktionen
```python
def addieren(x, y):
    return x + y

def subtrahieren(x, y):
    return x - y

def multiplizieren(x, y):
    return x * y

def dividieren(x, y):
    if y == 0:
        print("Division durch Null ist nicht erlaubt!")
        return None
    return x / y
```


## Main funktion

```python 
while True:
    try:
        # Eingabe der Zahlen
        num1 = float(input("Geben Sie die erste Zahl ein: "))
        num2 = float(input("Geben Sie die zweite Zahl ein: "))

        # Auswahl der Operation
        operation = input("Wählen Sie eine Operation (addieren/subtrahieren/multiplizieren/dividieren): ").lower()

        # Durchführung der Operation
        if operation == "addieren":
            print(f"Ergebnis: {addieren(num1, num2)}")
        elif operation == "subtrahieren":
            print(f"Ergebnis: {subtrahieren(num1, num2)}")
        elif operation == "multiplizieren":
            print(f"Ergebnis: {multiplizieren(num1, num2)}")
        elif operation == "dividieren":
            ergebnis = dividieren(num1, num2)
            if ergebnis is not None:
                print(f"Ergebnis: {ergebnis}")
        else:
            print("Ungültige Operation.")

    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")

    weitermachen = input("Möchten Sie eine weitere Berechnung durchführen? (ja/nein): ").lower()
    if weitermachen != "ja":
        break
```


## Erweiterung der Aufgabe - erster Library Import
Im folgenden verwenden wir zum ersten mal eine Library.
Ziel ist es unseren Taschenrechner grafisch anzuzeigen.

```python
import tkinter as tk
from tkinter import simpledialog, messagebox

def addieren(x, y):
    return x + y

def subtrahieren(x, y):
    return x - y

def multiplizieren(x, y):
    return x * y

def dividieren(x, y):
    if y == 0:
        messagebox.showerror("Fehler", "Division durch Null ist nicht erlaubt!")
        return None
    return x / y

def berechne():
    try:
        num1 = float(simpledialog.askfloat("Eingabe", "Geben Sie die erste Zahl ein:"))
        num2 = float(simpledialog.askfloat("Eingabe", "Geben Sie die zweite Zahl ein:"))
        operation = simpledialog.askstring("Eingabe", "Wählen Sie eine Operation (addieren/subtrahieren/multiplizieren/dividieren):").lower()

        if operation == "addieren":
            ergebnis = addieren(num1, num2)
        elif operation == "subtrahieren":
            ergebnis = subtrahieren(num1, num2)
        elif operation == "multiplizieren":
            ergebnis = multiplizieren(num1, num2)
        elif operation == "dividieren":
            ergebnis = dividieren(num1, num2)
        else:
            messagebox.showerror("Fehler", "Ungültige Operation.")
            return

        messagebox.showinfo("Ergebnis", f"Ergebnis: {ergebnis}")

    except ValueError:
        messagebox.showerror("Fehler", "Bitte geben Sie eine gültige Zahl ein.")

def main():
    root = tk.Tk()
    root.title("GUI Taschenrechner")
    btn = tk.Button(root, text="Starten", command=berechne)
    btn.pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    main()

```

