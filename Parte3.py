import pandas as pd

data = pd.read_csv('heart_failure_clinical_records_dataset.csv')

tipos_de_datos = data.dtypes
print("Tipos de datos en cada columna:")
print(tipos_de_datos)
print()
fumadores_por_genero = data.groupby(['sex', 'smoking']).size().unstack()
fumadores_por_genero.columns = ['No fumadores', '   Fumadores']

print("Cantidad de hombres y mujeres fumadores:")
print()
print(fumadores_por_genero)