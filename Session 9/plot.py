import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./titanic3.xls')

sex_counts = df['sex'].value_counts()

plt.figure(figsize=(8, 6))
sex_counts.plot.pie(autopct='%1.1f%%', startangle=90, labels=sex_counts.index)
plt.title('Verteilung von Geschlecht')
plt.ylabel('')  # Dies entfernt den Spaltennamen 'sex' von der Y-Achse
plt.show()
