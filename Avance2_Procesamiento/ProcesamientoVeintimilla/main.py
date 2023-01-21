import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Funcion para leer archivo
def leer_archivo(nombre_archivo):

    # -------------------- Diccionarios ------------------
    dic_anios = {}
    dic_tags =  {}  
    # ----------------------------------------------------
    #--------------------- contadores de anios -----------
    cont_2009 = 0
    cont_2010 = 0
    cont_2011 = 0
    cont_2012 = 0
    cont_2013 = 0
    cont_2014 = 0
    cont_2015 = 0
    cont_2016 = 0
    cont_2017 = 0
    cont_2018 = 0
    cont_2019 = 0
    cont_2020 = 0
    cont_2021 = 0
    # ----------------------------------------------------
    # --------------------Contadores de tags -------------
    cont_javascript = 0


    # ---------------------------------------------------


    archivo = open(nombre_archivo, encoding="utf8")
    
    lineas = archivo.readlines()

    contador = 0

    # Loop para leer cada linea
    for linea in lineas:
        print("-------------------- Inicio elem for")
        contador += 1
        linea.strip()
        info_linea = linea.split(',')
        pregunta = info_linea[0]
        anio = info_linea[1]
        tag = info_linea[2]
        tag = tag.replace('[', ' ')
        tag = tag.replace(']', ' ')
        tag = tag.replace(' ', '')

        if((contador > 1) and (anio != "/a") and (2009 == int(anio))):
            print("entró")
            cont_2009 = cont_2009 + 1

        if((contador > 1) and (anio != "/a") and (2010 == int(anio))):
            cont_2010 = cont_2010 + 1

        if((contador > 1) and (anio != "/a") and (2011 == int(anio))):
            cont_2011 = cont_2011 + 1

        if((contador > 1) and (anio != "/a") and (2012 == int(anio))):
            cont_2012 = cont_2012 + 1

        if((contador > 1) and (anio != "/a") and (2013 == int(anio))):
            cont_2013 = cont_2013 + 1

        if((contador > 1) and (anio != "/a") and (2014 == int(anio))):
            cont_2014 = cont_2014 + 1

        if((contador > 1) and (anio != "/a") and (2015 == int(anio))):
            cont_2015 = cont_2015 + 1

        if((contador > 1) and (anio != "/a") and (2016 == int(anio))):
            cont_2016 = cont_2016 + 1
        
        if((contador > 1) and (anio != "/a") and (2017 == int(anio))):
            cont_2017 = cont_2017 + 1

        if((contador > 1) and (anio != "/a") and (2018 == int(anio))):
            cont_2018 = cont_2018 + 1

        if((contador > 1) and (anio != "/a") and (2019 == int(anio))):
            cont_2019 = cont_2019 + 1

        if((contador > 1) and (anio != "/a") and (2020 == int(anio))):
            cont_2020 = cont_2020 + 1

        if((contador > 1) and (anio != "/a") and (2021 == int(anio))):
            cont_2021 = cont_2021 + 1




        print(cont_2009)
        print(anio)
        print("--------------------- Fin elem for ----------------------")
    # -----------------------------------------------
    dic_anios[2009] = cont_2009
    dic_anios[2010] = cont_2010
    dic_anios[2011] = cont_2011
    dic_anios[2012] = cont_2012
    dic_anios[2013] = cont_2013
    dic_anios[2014] = cont_2014
    dic_anios[2015] = cont_2015
    dic_anios[2016] = cont_2016
    dic_anios[2017] = cont_2017
    dic_anios[2018] = cont_2018
    dic_anios[2019] = cont_2019
    dic_anios[2020] = cont_2020
    dic_anios[2021] = cont_2021

    return dic_anios


#Funcion para grafico 1
def grafico_Uno(diccionario_uno):
    dataFrame = pd.DataFrame(list(diccionario_uno.items()))
    dataFrame.columns = ["Anio", "Cantidad preguntas"]
    print("Data frame de dic")
    print(dataFrame)

    #Inicializar el grafico
    plt.figure(figsize=(20, 10))
    ax = plt.subplot(111, polar=True)
    plt.axis('off')

    # Set the coordinates limits
    upperLimit = 150
    lowerLimit = 10
    labelPadding = 4

    max = dataFrame["Cantidad preguntas"].max()
    print(max)

    slope = (max - lowerLimit) / max
    heights = slope * dataFrame.Value + lowerLimit

    width = 2*np.pi / len(dataFrame.index)

    indexes = list(range(1, len(dataFrame.index)+1))
    angles = [element * width for element in indexes]
    angles

    # Draw bars
    bars = ax.bar(
        x=angles, 
        height=heights, 
        width=width, 
        bottom=lowerLimit,
        linewidth=2, 
        edgecolor="white")

    plt.show()


def grafico_Tres(diccionario_tres):
    plt.bar(list(diccionario_tres.keys()), diccionario_tres.values(), color='red')
    plt.xlabel("Años")
    plt.ylabel("Cantidad de preguntas")
    plt.show()

diccionario = leer_archivo("dataset-Veintimilla.csv")
print("Diccionario de años")
print(diccionario)
#grafico_Uno(diccionario)
grafico_Tres(diccionario)