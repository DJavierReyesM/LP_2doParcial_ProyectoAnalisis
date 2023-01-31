import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics
import plotly.express as px

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
    cont_python = 0
    cont_java = 0
    cont_c = 0
    cont_php = 0
    cont_android = 0
    cont_html = 0
    cont_jquery = 0
    cont_c_mas_mas = 0
    cont_css = 0
    # ---------------------------------------------------


    archivo = open(nombre_archivo, encoding="utf8")
    
    lineas = archivo.readlines()

    contador = 0

    # Loop para leer cada linea
    for linea in lineas:
        #print("-------------------- Inicio elem for")
        contador += 1
        linea.strip()
        info_linea = linea.split(',')
        #pregunta = info_linea[0]
        anio = info_linea[0]
        tag = info_linea[1]
        tag = tag.replace('[', ' ')
        tag = tag.replace(']', ' ')
        tag = tag.replace(' ', '').strip()
        
        #------------------------------Años---------------------------
        if((contador > 1) and (anio != "/a") and (2009 == int(anio))):
            #print("entró")
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
        #-------------------------------------------------------------

        #----------------------------Tags-----------------------------
        if((contador > 1) and (tag == "javascript") and (anio != "/a") and (int(anio) >= 2017) and (int(anio) <= 2021)):
            cont_javascript = cont_javascript + 1

        if((contador > 1) and (tag == "python") and (anio != "/a") and (int(anio) >= 2017) and (int(anio) <= 2021)):
            cont_python = cont_python + 1
        
        if((contador > 1) and (tag == "java") and (anio != "/a") and (int(anio) >= 2017) and (int(anio) <= 2021)):
            cont_java = cont_java + 1

        if((contador > 1) and (tag == "c") and (anio != "/a") and (int(anio) >= 2017) and (int(anio) <= 2021)):
            cont_c = cont_c + 1

        if((contador > 1) and (tag == "php") and (anio != "/a") and (int(anio) >= 2017) and (int(anio) <= 2021)):
            cont_php = cont_php + 1

        if((contador > 1) and (tag == "android") and (anio != "/a") and (int(anio) >= 2017) and (int(anio) <= 2021)):
            cont_android = cont_android + 1

        if((contador > 1) and (tag == "html") and (anio != "/a") and (int(anio) >= 2017) and (int(anio) <= 2021)):
            cont_html = cont_html + 1

        if((contador > 1) and (tag == "jquery") and (anio != "/a") and (int(anio) >= 2017) and (int(anio) <= 2021)):
            cont_jquery = cont_jquery + 1

        if((contador > 1) and (tag == "c++") and (anio != "/a") and (int(anio) >= 2017) and (int(anio) <= 2021)):
            cont_c_mas_mas = cont_c_mas_mas + 1

        if((contador > 1) and (tag == "css") and (anio != "/a") and (int(anio) >= 2017) and (int(anio) <= 2021)):
            cont_css = cont_css + 1

        #-------------------------------------------------------------


        #print("--------------------- Fin elem for ----------------------")
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

    dic_tags["javascript"] = cont_javascript
    dic_tags["python"] = cont_python
    dic_tags["java"] = cont_java
    dic_tags["c"] = cont_c
    dic_tags["php"] = cont_php
    dic_tags["android"] = cont_android
    dic_tags["html"] = cont_html
    dic_tags["jquery"] = cont_jquery
    dic_tags["c++"] = cont_c_mas_mas
    dic_tags["css"] = cont_css

    return dic_anios, dic_tags


#Funcion para grafico 1
def grafico_Uno(ax, labels : list, data : list, cmap : str, label_spacing : float, hole_size = 0):
    
    ax.axis('off')

    map = plt.get_cmap(cmap)

    bars_color = [map(i/len(labels)) for i in range(1, len(labels)+1)]

    #second part
    width = 2*np.pi / len(labels)

    indexes = list(range(1, len(labels)+1))
    angles = [element * width for element in indexes]

    bars = ax.bar(
        x = angles,
        height = data,
        width = width,
        bottom = hole_size,
        linewidth = 8, #era 2
        edgecolor = "white",
        color = bars_color)

    #insert labels
    labelPadding = statistics.mean(data) * label_spacing

    
    for reversed_index, bar, angle, height, label, value in zip([i for i in range(len(data), 0, -1)], bars, angles, data, labels, data):
        value_label_size = -(np.log10(165-(reversed_index/len(data))*164)**2)+15

        rotation = np.rad2deg(angle)

        if angle >= np.pi/2 and angle < 3*np.pi/2:
            alignment = "right"
            rotation = rotation + 180
        else: alignment = "left"

        #años
        ax.text(
            x = angle,
            y = 280, #bar.get_height() + labelPadding
            s = label,
            ha = alignment,
            va = 'center',
            rotation = rotation,
            rotation_mode = 'anchor',
            weight = 'heavy',
            size = 10)
        
        #red numbers
        ax.text(
            x = angle,
            y = 150, #bar.get_height()/2
            s = value,
            ha = alignment,
            va = 'center',
            rotation = rotation,
            rotation_mode = 'anchor',
            weight = 'heavy',
            size = 10,#value_label_size
            backgroundcolor = 'red',
        )

    #barra_color = fig.colorbar()
        
    plt.show()


#Funcion para gráfico tres
def grafico_Tres(diccionario_tres):
    plt.bar(list(diccionario_tres.keys()), diccionario_tres.values(), color='red')
    plt.xlabel("Años")
    plt.ylabel("Cantidad de preguntas")
    plt.show()


#--------------------------------------------------- Main ---------------------------------------------------------
arreglo_anios = []
arreglo_valores = []
arreglo_tags = []
arreglo_cantidad = []

diccionario, diccionario_tags = leer_archivo("dataset-Veintimilla.csv")

for key in diccionario:
    arreglo_anios.append(key)
    arreglo_valores.append(diccionario[key])

diccionario_tags_ordenado = sorted(diccionario_tags.items(), key=lambda x:x[1], reverse=True)
diccionario_tags_ordenado = dict(diccionario_tags_ordenado)

for key in diccionario_tags_ordenado:
    arreglo_tags.append(key)
    arreglo_cantidad.append(diccionario_tags[key])


print("Dic tags")
print(diccionario_tags)
#------------------------------------------------Respuesta pregunta 1----------------------------------------------
plt.figure(facecolor='white', figsize= (10, 10))
ax = plt.subplot(1,1,1, polar = True)
#labels = ['Milan', 'New York', 'Bologna', 'Miami', 'California', 'London', 'Paris','San Francisco', 'Zurich', 'Berlin']
#data = [150,140,130,110,95,87,80,78, 74,70]
#grafico_Uno(ax, labels=arreglo_anios, data = arreglo_valores, cmap = 'cool', label_spacing=0.20, hole_size = 50)
#label_spacing=0.10 hole_size = 10
#-------------------------------------------------------------------------------------------------------------------

#------------------------------------------------Respuesta pregunta 2----------------------------------------------
datos = dict(
    number = arreglo_cantidad,
    stage = arreglo_tags
)
fig = px.funnel(datos, x = "number", y = "stage")
fig.show()



#-------------------------------------------------------------------------------------------------------------------

#------------------------------------------------Respuesta pregunta 3----------------------------------------------
#Respuesta pregunta 3
#grafico_Tres(diccionario)


#-------------------------------------------------------------------------------------------------------------------