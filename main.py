import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp

data = pd.read_csv("Dados exp 5 - Página2.csv")

#Obtem eixos e incertezas
concentration = data["Concentração"].apply(lambda x: np.float64(eval(x)))
final_v = pd.to_numeric(data["Velocidade final"].str.replace(",","."))
v_uncertainty = data["Incerteza estatística (velocidade)"].str.replace(",", ".")
v_uncertainty = pd.to_numeric(v_uncertainty, errors="coerce")

# Definir o intervalo do domínio da função logarítmica
x_values = np.linspace(0, max(concentration)+0.2, 100)

# Ajustar os parâmetros da função logarítmica para estar no intervalo dos raios
a = (max(final_v) - min(final_v)) / (np.log(max(concentration)) - np.log(min(concentration)))
b = min(final_v) - a * np.log(min(concentration))

# Definir a função logarítmica ajustada
def log_function(x, a, b):
    return a * np.log(x) + b

# Gerar valores de y usando a função logarítmica
log_radius = log_function(x_values, a, b)


plt.errorbar(concentration, final_v, marker='o', linestyle="", yerr=v_uncertainty, color="red", label="Experimental Data")
plt.plot(x_values, log_radius, '-', label="Função Logarítmica Ajustada", color="blue")

plt.ylabel("Velocity (m/s)")
plt.xlabel("Concentration")
plt.title("Raio (m) por Velocidade de Dispersão (Escala Linear)")
plt.legend(loc="lower right")
plt.grid(True,linestyle="--",linewidth=0.5)
plt.xlim(0,0.52)
plt.ylim(0.04,0.21)
plt.show()



print(data.info())