import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


df = pd.read_csv("superstore.csv", encoding="unicode_escape")
x = df["Ship Mode"]
y= df["Sales"]
# Crear gráfico de barras
plt.bar(x, y, color="skyblue")   #Se crea un gráfico de barras utilizando la funcion bar 
plt.title("Gráfico de Barras")  #Se establece el el titulo gráfico
plt.xlabel("Categorías")    #El eje X representa, esto se refeleja bajo las barras
plt.ylabel("Valores")   #Las barras representan el eje Y
plt.show()      #Se  muestra el gráfico en una ventana

#- - - - - - - -- - -- -- - - - - - - - -- - - - - - - - - - - - - - -- - - - - - -- -  - -- -

# Datos de ejemplo
datos = df["Region"]

# Crear histograma
plt.hist(datos, bins=5, color="orange", edgecolor="black")
plt.title("Histograma")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.show()
            