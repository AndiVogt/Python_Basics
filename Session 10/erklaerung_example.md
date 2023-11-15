# Titanic Datenanalyse in Python

In diesem Dokument analysieren wir die Titanic-Daten mit Python. Wir verwenden `pandas` für die Datenmanipulation und `matplotlib` für die Visualisierung.

## Einlesen der Daten

Zuerst importieren wir die notwendigen Bibliotheken und lesen die Daten ein:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../Session 9/titanic3.xls')
```

- ``pandas`` wird als ``pd`` importiert, eine gängige Konvention in Python.
- ``matplotlib.pyplot`` wird als ``plt`` importiert, um Diagramme zu erstellen.
- Die Titanic-Daten werden aus einer Excel-Datei in einen DataFrame ``df`` eingelesen.
## 1. Grundlegende Statistiken

```python
pclass_counts = df['pclass'].value_counts()
pclass_counts.plot(kind='bar')
plt.title('Anzahl der Passagiere in jeder Klasse')
plt.show()

print(df['age'].mean())
print(df['fare'].mean())
```

- ``df['pclass'].value_counts()`` zählt, wie viele Passagiere in jeder Klasse (1., 2., 3.) sind.
- ``.plot(kind='bar')`` erstellt ein Balkendiagramm dieser Zählungen.
- ``df['age'].mean()`` und ``df['fare'].mean()`` berechnen das Durchschnittsalter und den durchschnittlichen Ticketpreis.

## 2. Verteilungen und Überlebensraten
```python
pclass_survival = df.groupby('pclass')['survived'].mean()
pclass_survival.plot(kind='bar')
plt.title('Überlebensrate nach Klasse')
plt.show()

sex_survival = df.groupby('sex')['survived'].mean()
sex_survival.plot(kind='bar')
plt.title('Überlebensrate nach Geschlecht')
plt.show()

df[df['survived'] == 1]['age'].hist(alpha=0.5, label='Überlebende')
df[df['survived'] == 0]['age'].hist(alpha=0.5, label='Nicht-Überlebende')
plt.legend()
plt.title('Altersverteilung der Überlebenden und Nicht-Überlebenden')
plt.show()
```

- ``df.groupby('pclass')['survived'].mean()`` berechnet die durchschnittliche Überlebensrate in jeder Klasse.
- ``df.groupby('sex')['survived'].mean()`` macht dasselbe, aber basierend auf dem Geschlecht.
Histogramme für das Alter der Überlebenden und Nicht-Überlebenden werden erstellt, um die Altersverteilung zu vergleichen.

## 3. Korrelationen
```python
print(df[['age', 'fare']].corr())
print(df[['pclass', 'fare']].corr())
```
- ``.corr()`` berechnet die Korrelation zwischen den Spalten. Werte nahe 1 oder -1 zeigen eine starke positive bzw. negative Korrelation.

## 4. Fortgeschrittene Analysen
```python
embarked_survival = df.groupby('embarked')['survived'].mean()
embarked_survival.plot(kind='bar')
plt.title('Überlebensrate basierend auf dem Abfahrthafen')
plt.show()

sibsp_survival = df.groupby('sibsp')['survived'].mean()
sibsp_survival.plot(kind='bar')
plt.title('Überlebensrate basierend auf der Anzahl der Geschwister/Ehepartner')
plt.show()

parch_survival = df.groupby('parch')['survived'].mean()
parch_survival.plot(kind='bar')
plt.title('Überlebensrate basierend auf der Anzahl der Eltern/Kinder')
plt.show()
```

- Hier analysieren wir die Überlebensrate basierend auf dem Abfahrthafen (``embarked``), der Anzahl der Geschwister/Ehepartner (``sibsp``) und der Anzahl der Eltern/Kinder (``parch``).

## Zusätzliches Beispiel: Durchschnittlicher Ticketpreis für Überlebende vs. Nicht-Überlebende
```python
avg_fare_survival = df.groupby('survived')['fare'].mean()
avg_fare_survival.plot(kind='bar')
plt.title('Durchschnittlicher Ticketpreis für Überlebende vs. Nicht-Überlebende')
plt.show()
```
- Dieser Codeabschnitt vergleicht den durchschnittlichen Ticketpreis zwischen Überlebenden und Nicht-Überlebenden.