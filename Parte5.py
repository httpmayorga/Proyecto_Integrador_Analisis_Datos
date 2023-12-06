import pandas as pd
import requests
import io


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

    # Verificar y eliminar valores atípicos (ejemplo con la columna 'age')
    # Aquí puedes implementar lógica para detectar y eliminar valores atípicos en otras columnas también
    q1 = dataframe['age'].quantile(0.25)
    q3 = dataframe['age'].quantile(0.75)
    iqr = q3 - q1
    filtro_sin_atipicos = (dataframe['age'] >= q1 - 1.5 * iqr) & (dataframe['age'] <= q3 + 1.5 * iqr)
    dataframe = dataframe[filtro_sin_atipicos]

    # Crear columna de categorización por edades
    dataframe['categoria_edad'] = pd.cut(
        dataframe['age'],
        bins=[0, 12, 19, 39, 59, float('inf')],
        labels=['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    )

    return dataframe

# Función que encapsula todas las operaciones
def procesar_datos(dataframe):
    limpio_y_categorizado = limpieza_y_categorizacion_datos(dataframe)
    nombre_archivo_salida = 'datos_procesados.csv'
    limpio_y_categorizado.to_csv(nombre_archivo_salida, index=False)
    print(f"Datos procesados y guardados en '{nombre_archivo_salida}'")

# Cargar datos descargados usando requests
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
response = requests.get(url_datos)
if response.status_code == 200:
    datos = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
    procesar_datos(datos)
else:
    print(f"Error al descargar los datos. Código de estado: {response.status_code}")
