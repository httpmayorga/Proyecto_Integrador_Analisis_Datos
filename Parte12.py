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
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score


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
rf_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)  
rf_model.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = rf_model.predict(X_test)

# Calcular la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de Confusión:")
print(conf_matrix)

# Calcular el accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión (Accuracy): {accuracy:.4f}")

# Calcular el F1-Score
f1 = f1_score(y_test, y_pred)
print(f"F1-Score: {f1:.4f}")