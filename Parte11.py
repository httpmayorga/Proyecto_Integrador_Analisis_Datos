from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import plotly.graph_objs as go
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

data = pd.read_csv('datos_procesados.csv')

class_counts = data['DEATH_EVENT'].value_counts()

# Graficar la distribución de clases
plt.figure(figsize=(6, 4))
class_counts.plot(kind='bar', color=['blue', 'red'])
plt.title('Distribución de Clases')
plt.xlabel('Clases')
plt.ylabel('Cantidad')
plt.xticks([0, 1], ['Vivos', 'Fallecidos'], rotation=0)  # Etiquetas en el eje x
plt.show()

data = data.drop('categoria_edad', axis=1)

# Definir las características (X) y la variable objetivo (y)
X = data.drop('DEATH_EVENT', axis=1)
y = data['DEATH_EVENT']

# Realizar la partición estratificada en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Ajustar un árbol de decisión
tree = DecisionTreeClassifier(max_depth=6, random_state=42) #Parametro en 6 
tree.fit(X_train, y_train)

# Predecir sobre el conjunto de test
y_pred = tree.predict(X_test)
matrizconfusion= confusion_matrix(y_test, y_pred)

# Calcular la precisión (accuracy)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del árbol de decisión: {accuracy:.4f}")
print(f"Matriz de confucion:")
print(matrizconfusion)