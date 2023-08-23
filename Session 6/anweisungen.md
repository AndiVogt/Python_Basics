# Aufgabe:
Schreibe ein Python-Programm, das ein einfaches Rechenspiel implementiert. Das Spiel soll den Benutzer dazu auffordern, eine Reihe von Additionen zu lösen, bis die richtige Antwort gegeben wird.

Erstelle ein einfaches Rechenspiel, bei dem der Benutzer Additionen lösen muss, bis er die richtige Antwort gibt. 
Das Spiel soll mit einer Endlosschleife (while True) und einer Schleifenunterbrechung (break) implementiert werden. 
Der Benutzer soll über die Konsole einen Nutzer-Input geben können und die eingegebene Antwort wird überprüft. 
Wenn die Antwort richtig ist, wird die Schleife unterbrochen und eine Erfolgsmeldung wird ausgegeben.


# Vorgehensweise:
1. Definiere zwei feste Variablen (z.B. 3 und 5)
2. Erstelle eine Schleife, welche so lange läuft, bis ein abbrechendes Ereignis eintritt
3. Frage den Nutzer mit Hilfe eines prints was die Summe von Variable 1 und 2 ist. 
Achte hierbei darauf die Zahlen in der Aufforderung nicht zu "Hard coden", sprich greife auf die Variablen zu. 
Nutze hierzu f-Strings. z.B. `f"Du bist {variable} alt"`
4. Fordere nun den Nutzer zur Eingabe seiner Antwort auf.
5. Überprüfe ob der Nutzer das richtige Ergebnis berechnet hat. Nutze Kontrollstrukturen
6. Bei richtiger Antwort bestätige dies kurz und brich die Schleife ab.
7. Bei falscher Antwort teile dem Nutzer mit, dass er es erneut versuchen soll. Hier soll der gesamte Prozess von vorn beginnen.
8. Nach der Schleife teile dem Nutzer mit, dass das Programm beendet ist.

## Zusatz:
Schreibe das Programm so um, dass zuerst nach den 2 Zahlen gefragt wird die zusammen gerechnet werden sollen !