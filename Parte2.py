import pandas as pd

data = pd.read_csv('heart_failure_clinical_records_dataset.csv')

fallecidos = data[data['DEATH_EVENT'] == 1]
sobrevivientes = data[data['DEATH_EVENT'] == 0]

promedio_fallecidos = fallecidos['age'].mean()
promedio_sobrevivientes = sobrevivientes['age'].mean()

print(f"El promedio de edad de las personas fallecidas es: {promedio_fallecidos:.2f} años")
print(f"El promedio de edad de las personas sobrevivientes es: {promedio_sobrevivientes:.2f} años")
