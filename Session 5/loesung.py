num1 = 5
num2 = 3

while True:
    print(f"Was ist die Summe von {num1} und {num2} ?")
    user_answer = int(input("Deine Antwort: "))

    if user_answer == num1 + num2:
        print("Richtig!")
        break
    else:
        print("Falsch! Versuche es erneut.")

print("Das Spiel ist beendet. Gut gemacht!")
