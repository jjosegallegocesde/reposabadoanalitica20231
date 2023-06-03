import pandas as pd
import matplotlib.pyplot as plt

def calcularPromedioSalariosPorEdad(dataframe,rangos,columnaInteres,columnaPromediar,nombreGrafica):
    plt.figure()

    #crear un columna nueva por rangos de edad
    dataframe['rangosEdad']=pd.cut(dataframe[columnaInteres],bins=rangos)
    #calcular la suma de los salarios por rango de edad
    salarioPorRango=dataframe.groupby('rangosEdad')[columnaPromediar].sum()

    #definimos los datos a garficar
    salario=salarioPorRango.values
    rangosEdad=salarioPorRango.index

    plt.pie(salario, labels=rangosEdad, autopct='%1.1f%%' )
    plt.title("Salarios por ragngo de edad")

    plt.savefig(f'./assets/img/{nombreGrafica}.png')