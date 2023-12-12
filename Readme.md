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

Parte 7: Visualización de Datos con Matplotlib
Una vez que los datos se exportaron mediante el script de Extracción, Transformación y Carga (ETL), se realiza la visualización con Matplotlib. En esta sección, se utilizan diferentes gráficos para analizar los datos:

-Histograma de Distribución de Edades: Se representa la distribución de edades mediante un histograma para comprender mejor cómo están distribuidas las edades en el conjunto de datos.
-Histogramas Agrupados por Género: Se muestran histogramas separados para hombres y mujeres, representando la cantidad de anémicos, diabéticos, fumadores y muertos en cada grupo. Esto permite comparar las distribuciones entre géneros para cada condición médica y la mortalidad.

Parte 8: Gráficas de Torta con Subplots
Usando el mismo DataFrame, se generan gráficas de torta utilizando subplots. Cada subplot representa la distribución de:

-Cantidad de Anémicos
-Cantidad de Diabéticos
-Cantidad de Fumadores
-Cantidad de Muertos

Al presentar estas distribuciones en subplots, se facilita la comparación entre las diferentes categorías, permitiendo una visualización más clara y comparativa.

Parte 9: Gráfico de Dispersión 3D con Plotly
En esta sección, se implementa un gráfico de dispersión en tres dimensiones (3D) utilizando Plotly. El objetivo es visualizar la distribución de datos reducidos en un espacio tridimensional generado por t-SNE (t-distributed Stochastic Neighbor Embedding). Los puntos en el gráfico representan observaciones del conjunto de datos, diferenciados por la clase 'Muerto' o 'Vivo' (indicado por colores), lo que permite observar la agrupación o dispersión de los datos en tres dimensiones y su relación con la clase objetivo 'DEATH_EVENT'.


Parte 10: Predicción de datos de una columna

Se utiliza regresión lineal para estimar valores faltantes en la columna 'age'.
Se eliminan columnas no necesarias ('DEATH_EVENT', 'age', 'categoria_edad').
Se ajusta un modelo para predecir edades basado en otras columnas.
Se evalúa el rendimiento del modelo usando error cuadrático medio (MSE).

Parte 11: Clasificación

Se analiza la distribución de clases en el conjunto de datos.
Se divide el conjunto en entrenamiento y prueba de forma estratificada.
Se ajusta un árbol de decisión y se evalúa la precisión en el conjunto de prueba.

Parte 12: Modelo de Random Forest

Se entrena un modelo de Random Forest.
Se calcula la matriz de confusión, precisión (accuracy) y F1-Score.
Se considera si el accuracy captura completamente el rendimiento del modelo.
