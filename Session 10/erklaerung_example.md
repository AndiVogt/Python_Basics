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
```
![alt text](assets/passengers_per_class.png)
```python
print(df['age'].mean())
print(df['fare'].mean())
```
Output:
```
29.8811345124283
33.29547928134557
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
```
![alt text](assets/survived_per_class.png)
```python
sex_survival = df.groupby('sex')['survived'].mean()
sex_survival.plot(kind='bar')
plt.title('Überlebensrate nach Geschlecht')
plt.show()
```
![alt text](assets/survived_per_sex.png)
```python
df[df['survived'] == 1]['age'].hist(alpha=0.5, label='Überlebende')
df[df['survived'] == 0]['age'].hist(alpha=0.5, label='Nicht-Überlebende')
plt.legend()
plt.title('Altersverteilung der Überlebenden und Nicht-Überlebenden')
plt.show()
```
![alt text](assets/age_of_survived.png)

- ``df.groupby('pclass')['survived'].mean()`` berechnet die durchschnittliche Überlebensrate in jeder Klasse.
- ``df.groupby('sex')['survived'].mean()`` macht dasselbe, aber basierend auf dem Geschlecht.
Histogramme für das Alter der Überlebenden und Nicht-Überlebenden werden erstellt, um die Altersverteilung zu vergleichen.

## 3. Korrelationen
```python
print(df[['age', 'fare']].corr())
print(df[['pclass', 'fare']].corr())
```
Output:
```
           age      fare
age   1.000000  0.178739
fare  0.178739  1.000000
          pclass      fare
pclass  1.000000 -0.558629
fare   -0.558629  1.000000
```
- ``.corr()`` berechnet die Korrelation zwischen den Spalten. Werte nahe 1 oder -1 zeigen eine starke positive bzw. negative Korrelation.

## 4. Fortgeschrittene Analysen
```python
embarked_survival = df.groupby('embarked')['survived'].mean()
embarked_survival.plot(kind='bar')
plt.title('Überlebensrate basierend auf dem Abfahrthafen')
plt.show()
```
![alt text](assets/survived_based_on_embarked.png)
```python
sibsp_survival = df.groupby('sibsp')['survived'].mean()
sibsp_survival.plot(kind='bar')
plt.title('Überlebensrate basierend auf der Anzahl der Geschwister/Ehepartner')
plt.show()
```
![alt text](assets/survived_partner_siblings.png)
```python
parch_survival = df.groupby('parch')['survived'].mean()
parch_survival.plot(kind='bar')
plt.title('Überlebensrate basierend auf der Anzahl der Eltern/Kinder')
plt.show()
```
![alt text](assets/survived_parents_childs.png)

- Hier analysieren wir die Überlebensrate basierend auf dem Abfahrthafen (``embarked``), der Anzahl der Geschwister/Ehepartner (``sibsp``) und der Anzahl der Eltern/Kinder (``parch``).

## Zusätzliches Beispiel: Durchschnittlicher Ticketpreis für Überlebende vs. Nicht-Überlebende
```python
avg_fare_survival = df.groupby('survived')['fare'].mean()
avg_fare_survival.plot(kind='bar')
plt.title('Durchschnittlicher Ticketpreis für Überlebende vs. Nicht-Überlebende')
plt.show()
```
![alt text](assets/ticketprice_survived.png)

- Dieser Codeabschnitt vergleicht den durchschnittlichen Ticketpreis zwischen Überlebenden und Nicht-Überlebenden.