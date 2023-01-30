# Avance: Preprocesamiento y Visualizacion
# Diego Reyes
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

archivo = "dataset_dreyes.csv"

#Lectura del Dataset
def leer_archivo(nombre_archivo):
    df = pd.read_csv(nombre_archivo)
    return df

# Función para visualización 1: Top 10 usuarios con más medallas de oro
def visual1(dataset):
    # Dataset ordenado en base a la cantidad de medallas de oro
    ordered_df = dataset.sort_values(by='N_oro', ascending=False)
    ordered_df.reset_index(inplace=True)
    print("Dataset ordenado por medallas de oro")
    print(ordered_df.to_string())
    # Dataset con Top 10 usuarios con medallas de oro
    medallas10 = ordered_df[:10][::-1]
    print("\nDataset con Top 10 usuarios con más medallas de oro")
    print(medallas10[::-1].to_string())
    # Rango de valores para el gráfico
    my_range = range(1, len(medallas10.index) + 1)
    medallas10.reset_index(inplace=True)
    # Se define la estructura del gráfico (tamaño, estructura de lineas, etc.)
    plt.figure(figsize=(13, 6))
    plt.hlines(y=my_range, xmin=0, xmax=medallas10['N_oro'], color='skyblue')
    plt.plot(medallas10['N_oro'], my_range, "o", alpha=0.4, zorder=0)
    # Se añaden titulos
    plt.yticks(my_range, medallas10['Nombre'])
    plt.title("Top 10 usuarios de StackOverflow con más medallas de Oro", loc='center')
    plt.xlabel('Cantidad de medallas de Oro')
    plt.ylabel('Usuarios')
    for row in medallas10.itertuples():
        plt.text(row.N_oro, row.Index+0.5, row.N_oro, horizontalalignment='center', verticalalignment='bottom',
                fontsize=9)
    plt.show()

def visual2(dataset):
    # Se aplican los filtros de "país" = "Not provided by the user" y "reputación" <= 350000
    df = dataset[(dataset["Pais"]=="Not provided by the user") & (dataset["Reputacion"]<=350000)]
    # Se ordena el dataset en función a las medallas de plata
    ordered_df = df.sort_values(by='N_plata', ascending=False)
    ordered_df.reset_index(inplace=True)
    print("Dataset: Ordenado por medallas de plata tras la aplicación de los filtros anteriores: (StacKOverflow)")
    print(ordered_df.to_string())
    medallasplata = ordered_df[:10]
    print("\nDataset con Top 10 usuarios con más medallas de plata (sin info. de ubicación proporcionada y con reputación <= 350000)")
    print(medallasplata.to_string())
    # Se añaden valores a 2 listas, users y medals, para construir la gráfica
    users = []
    medals = []
    for i in range(len(medallasplata)):
        users.append(medallasplata.iloc[i]["Nombre"])
        medals.append(medallasplata.iloc[i]["N_plata"])

    # Se construye la gráfica con las listas creadas anteriormente
    plt.figure(figsize=(13.3, 6.3))
    plt.style.use('seaborn-darkgrid')
    plt.fill_between(users, medals, color="skyblue", alpha=0.3)
    plt.plot(users, medals, color="skyblue")
    # Se recorren las filas del dataset de medallasplata para añadir los valores de las medallas dentro de la gráfica
    for row in medallasplata.itertuples():
        plt.text(row.Index, row.N_plata, row.N_plata,horizontalalignment='center', verticalalignment='bottom',fontsize=10)
    plt.title("Top 10 usuarios con más medallas de plata (sin info. de ubicación proporcionada y con reputación <= 350000)", loc="left")
    plt.xlabel("Usuarios")
    plt.ylabel("# de Medallas de Plata")
    plt.show()

def visual3(dataset):
    total_medallas = []
    for i in range(len(dataset)):
        sumaMedallas = dataset.iloc[i]["N_oro"] + dataset.iloc[i]["N_plata"] + dataset.iloc[i]["N_bronce"]
        total_medallas.append(sumaMedallas)
    dataset["totalMedallas"] = total_medallas

    expresion2 = ".*Germany.*"
    dataset = dataset[(dataset.Pais.str.match(expresion2))]
    ordered_df = dataset.sort_values(by='totalMedallas', ascending=False)[:10][::-1]
    ordered_df.reset_index(inplace=True)
    print(ordered_df[::-1].to_string())

    bars1 = []
    bars2 = []
    bars3 = []
    names = []
    for i in range(len(ordered_df)):
        bars1.append(ordered_df.iloc[i]["N_bronce"])
        bars2.append(ordered_df.iloc[i]["N_plata"])
        bars3.append(ordered_df.iloc[i]["N_oro"])
        names.append(ordered_df.iloc[i]["Nombre"])
    # Se construye el gráfico
    bars = np.add(bars1, bars2).tolist()
    plt.figure(figsize=(13.3, 6.3))
    b1 = plt.barh(names, bars1, color="#e1c77b")
    b2 = plt.barh(names, bars2, left=bars1, color="#cac5b4")
    b3 = plt.barh(names, bars3, left= bars, color="#ecc349")

    plt.legend([b3, b2, b1], ["Oro", "Plata", "Bronce" ], title="Medallas", loc="lower right")
    plt.title("Top 10 usuarios de StackOverflow de Alemania con más medallas (Oro,Plata, Bronce)", loc='center')
    for i in range(len(ordered_df)):
        plt.text((ordered_df.iloc[i]["N_bronce"])/2,i - 0.2, ordered_df.iloc[i]["N_bronce"], horizontalalignment='center', verticalalignment='bottom',
                fontsize=9)
        plt.text((ordered_df.iloc[i]["N_bronce"])+(ordered_df.iloc[i]["N_plata"])/2, i - 0.2, ordered_df.iloc[i]["N_plata"], horizontalalignment='center',
                 verticalalignment='bottom',
                 fontsize=9)
        plt.text(ordered_df.iloc[i]["N_bronce"] + ordered_df.iloc[i]["N_plata"]+(ordered_df.iloc[i]["N_oro"])/2, i - 0.2, ordered_df.iloc[i]["N_oro"],
                 horizontalalignment='center',
                 verticalalignment='bottom',
                 fontsize=9)
    # Se muestra el gráfico
    plt.show()

dataset = leer_archivo(archivo)
#Gráfica 1
visual1(dataset)

#Gráfica 2
visual2(dataset)

#Gráfica 3
visual3(dataset)