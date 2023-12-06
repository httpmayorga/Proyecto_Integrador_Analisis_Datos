import requests
import pandas as pd
import io
import sys

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

    # Crear columna de categorización por edades
    dataframe['categoria_edad'] = pd.cut(
        dataframe['age'],
        bins=[0, 12, 19, 39, 59, float('inf')],
        labels=['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    )

    return dataframe

def procesar_datos(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            datos = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
            datos_procesados = limpieza_y_categorizacion_datos(datos)
            nombre_archivo_salida = 'datos_procesados.csv'
            datos_procesados.to_csv(nombre_archivo_salida, index=False)
            print(f"Datos procesados y guardados en '{nombre_archivo_salida}'")
        else:
            print(f"Error al descargar los datos. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Por favor, proporcione la URL como argumento al ejecutar el script.")
    else:
        url_datos = sys.argv[1]
        procesar_datos(url_datos)
