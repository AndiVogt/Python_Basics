import pandas as pd
import matplotlib.pyplot as plt

# Daten einlesen
df = pd.read_excel('../Session 9/titanic3.xls')

# 1. Grundlegende Statistiken
pclass_counts = df['pclass'].value_counts()
pclass_counts.plot(kind='bar')
plt.title('Anzahl der Passagiere in jeder Klasse')
plt.show()

print(df['age'].mean())
print(df['fare'].mean())

# 2. Verteilungen und Überlebensraten
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

# 3. Korrelationen
print(df[['age', 'fare']].corr())
print(df[['pclass', 'fare']].corr())

# 4. Fortgeschrittene Analysen
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

# Zusätzliches Beispiel: Durchschnittlicher Ticketpreis für Überlebende vs. Nicht-Überlebende
avg_fare_survival = df.groupby('survived')['fare'].mean()
avg_fare_survival.plot(kind='bar')
plt.title('Durchschnittlicher Ticketpreis für Überlebende vs. Nicht-Überlebende')
plt.show()
