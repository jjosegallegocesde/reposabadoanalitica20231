import pandas as pd
from data.data1 import apartamento1,apartamento2
from helpers.crearTablasHTML import crearTabla
from helpers.crearBarras import graficarPromedioSalarial
from helpers.crearTorta import calcularPromedioSalariosPorEdad

tabla1=pd.DataFrame(apartamento1,columns=['edad'])
tabla2=pd.DataFrame(apartamento2,columns=['edad'])
tabla3=pd.read_csv("./data/empleados.csv")

#EFECTUANDO FILTROS CON PYTHON

#1. DEFINIR UNA CONDICION LOGICA
empleadosJovenesAnalistas1=tabla3.query('cargo=="analista1"')
empleadosSalarioBajo=tabla3.query('salario<5000000 and cargo=="analista2"')
empleadosADespedir=tabla3.query('edad>=50')

#2. creamos la tabla html con el dataframe del filtro
crearTabla(empleadosJovenesAnalistas1,"tablaJovenes")
crearTabla(empleadosSalarioBajo,"tablabajossalarios")
crearTabla(empleadosADespedir,"tablaoportunidaddemejora")

#3. Genera gráficas
graficarPromedioSalarial(empleadosADespedir,'cargo','salario','graficajubilados')
calcularPromedioSalariosPorEdad(empleadosJovenesAnalistas1,[20,30,40,50,60],'edad','salario','graficadetortaanalisis1')
