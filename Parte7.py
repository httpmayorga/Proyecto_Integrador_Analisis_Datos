import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('heart_failure_clinical_records_dataset.csv')

def limpieza_y_categorizacion_datos(dataframe):
    # Verificar valores faltantes
    faltantes = dataframe.isnull().sum().sum()
    if faltantes > 0:
        print(f"¡Hay {faltantes} valores faltantes en el DataFrame!")
    else:
        print("No hay valores faltantes en el DataFrame.")

    # Verificar filas duplicadas
    duplicados = dataframe.duplicated().sum()
    if duplicados > 0:
        print(f"Hay {duplicados} filas duplicadas en el DataFrame.")
        dataframe.drop_duplicates(inplace=True)
    else:
        print("No hay filas duplicadas en el DataFrame.")

    # Verificar y eliminar valores atípicos

    q1 = dataframe['age'].quantile(0.25)
    q3 = dataframe['age'].quantile(0.75)
    iqr = q3 - q1
    filtro_sin_atipicos = (dataframe['age'] >= q1 - 1.5 * iqr) & (dataframe['age'] <= q3 + 1.5 * iqr)
    dataframe = dataframe[filtro_sin_atipicos]

    return dataframe

limpieza_y_categorizacion_datos(data)


plt.hist(data['age'], bins=15, color='skyblue', edgecolor='black')

plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.title('Distribución de Edades')

plt.show()

male_data = data[data['sex'] == 1]  # 1 representa a hombres
female_data = data[data['sex'] == 0]  # 0 representa a mujeres

# Calcular la cantidad de anémicos, diabéticos, fumadores y muertos por género
male_counts = [
    male_data['anaemia'].sum(),
    male_data['diabetes'].sum(),
    male_data['smoking'].sum(),
    male_data['DEATH_EVENT'].sum()
]

female_counts = [
    female_data['anaemia'].sum(),
    female_data['diabetes'].sum(),
    female_data['smoking'].sum(),
    female_data['DEATH_EVENT'].sum()
]

categories = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']


bar_width = 0.35
index = range(len(categories))

plt.bar(index, male_counts, bar_width, label='Hombres')
plt.bar([i + bar_width for i in index], female_counts, bar_width, label='Mujeres')


plt.xlabel('Categorías')
plt.ylabel('Cantidad')
plt.title('Comparación por género')
plt.xticks([i + bar_width / 2 for i in index], categories)
plt.legend()

plt.tight_layout()
plt.show()