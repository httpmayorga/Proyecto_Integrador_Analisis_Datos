import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]
edades = data["age"]

edades_np = np.array(edades)
promedio_edad = np.mean(edades_np)

print(f"El promedio de edad de las personas participantes es: {promedio_edad:.2f} años")
