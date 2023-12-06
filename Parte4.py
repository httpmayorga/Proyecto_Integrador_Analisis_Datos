import requests

def descargar_datos_csv_desde_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            nombre_archivo = url.split('/')[-1]
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(response.content)
            
            print(f"Datos descargados correctamente como '{nombre_archivo}'")
        else:
            print(f"Error al descargar los datos. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

# Llamar a la función con la URL del archivo CSV
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
descargar_datos_csv_desde_url(url_datos)
