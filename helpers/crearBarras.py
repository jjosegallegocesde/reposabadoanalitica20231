import matplotlib.pyplot as plt

def graficarPromedioSalarial(dataFrame,campoX,campoY,nombreGrafica):
    colores=['green','red','blue']
    salarioPromedio=dataFrame.groupby(campoX)[campoY].mean()

    #Generar la grafica
    plt.bar(salarioPromedio.index,salarioPromedio,color=colores)

    plt.title("PROMEDIO SALARIAL")
    plt.xlabel("Cargos")
    plt.ylabel("Salario Mensual")

    plt.savefig(f'./assets/img/{nombreGrafica}.png')