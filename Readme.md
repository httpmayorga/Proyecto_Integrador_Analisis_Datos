Proyecto de Análisis de Datos
Este proyecto se enfoca en el análisis de un conjunto de datos relacionados con fallo cardíaco, realizando una serie de tareas de procesamiento y análisis.

Parte 1: Introducción al Análisis de Datos
En esta sección se llevan a cabo las siguientes operaciones:

-Descarga y carga de un conjunto de datos sobre fallo cardíaco.
-Utilización de la librería datasets de Huggingface.
-Conversión de la lista de edades a un arreglo de NumPy y cálculo del promedio de edad de los participantes en el estudio.

Parte 2: Carga de Datos
Esta sección se encarga de:

-Convertir la estructura Dataset en un DataFrame de Pandas.
-Separar el DataFrame en dos conjuntos: personas fallecidas y sobrevivientes.
-Calcular los promedios de las edades de cada conjunto y mostrarlos.

Parte 3: Cálculo de Análisis Simples
Aquí se realizan las siguientes tareas:

-Verificación de los tipos de datos en cada columna del DataFrame.
-Cálculo de la cantidad de hombres fumadores y mujeres fumadoras utilizando agregaciones en Pandas.

Parte 4: Procesamiento de Información en Bruto
En esta sección, se lleva a cabo:

-Descarga de datos desde una URL específica utilizando requests.
-Escritura de la respuesta como un archivo de texto plano con extensión CSV.
-Creación de una función reutilizable para descargar datos de cualquier URL.

Parte 5: Limpieza de Datos
En esta etapa, se realiza lo siguiente:

-Verificar valores faltantes en el DataFrame.
-Eliminar filas duplicadas.
-Detectar y eliminar valores atípicos o inconsistentes.

Parte 6: Automatización del Procesamiento de Datos
Este apartado encapsula todas las operaciones anteriores en funciones reutilizables que procesan y categorizan los datos de forma automática, facilitando su uso en futuras iteraciones del proyecto.
