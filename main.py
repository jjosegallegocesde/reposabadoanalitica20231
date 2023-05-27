import pandas as pd
from data.data1 import apartamento1,apartamento2
from helpers.crearTablasHTML import crearTabla


tabla1=pd.DataFrame(apartamento1,columns=['edad'])
tabla2=pd.DataFrame(apartamento2,columns=['edad'])
tabla3=pd.read_csv("./data/empleados.csv")

#EFECTUANDO FILTROS CON PYTHON

#1. DEFINIR UNA CONDICION LOGICA
empleadosJovenesAnalistas1=tabla3.query('edad<28 and cargo=="analista1"')
empleadosSalarioBajo=tabla3.query('salario<5000000 and cargo=="analista2"')
empleadosADespedir=tabla3.query('edad>=50')

#2. creamos la tabla html con el dataframe del filtro
crearTabla(empleadosJovenesAnalistas1,"tablaJovenes")
crearTabla(empleadosSalarioBajo,"tablabajossalarios")
crearTabla(empleadosADespedir,"tablaoportunidaddemejora")

