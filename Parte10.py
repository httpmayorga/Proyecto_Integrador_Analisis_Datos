from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import plotly.graph_objs as go
import plotly.express as px

datapd = pd.read_csv('datos_procesados.csv')

def limpieza_y_categorizacion_datos(data):
    # Verificar valores faltantes
    faltantes = data.isnull().sum().sum()
    if faltantes > 0:
        print(f"¡Hay {faltantes} valores faltantes en el DataFrame!")
    else:
        print("No hay valores faltantes en el DataFrame.")

    # Verificar filas duplicadas
    duplicados = data.duplicated().sum()
    if duplicados > 0:
        print(f"Hay {duplicados} filas duplicadas en el DataFrame.")
        data.drop_duplicates(inplace=True)
    else:
        print("No hay filas duplicadas en el DataFrame.")

    # Verificar y eliminar valores atípicos
    for column in data.select_dtypes(include='number').columns:
        q1 = data[column].quantile(0.25)
        q3 = data[column].quantile(0.75)
        iqr = q3 - q1
        filtro_sin_atipicos = (data[column] >= q1 - 1.5 * iqr) & (data[column] <= q3 + 1.5 * iqr)
        data = data[filtro_sin_atipicos]

    return data

data_limpia=limpieza_y_categorizacion_datos(datapd)

columnas_a_eliminar = ['DEATH_EVENT', 'age', 'categoria_edad']
X = data_limpia.drop(columnas_a_eliminar, axis=1)
y = data_limpia['age']

modelo_regresion = LinearRegression()
modelo_regresion.fit(X, y)


edades_predichas = modelo_regresion.predict(X)

mse = mean_squared_error(y, edades_predichas)
print(f"El error cuadrático medio es: {mse}")