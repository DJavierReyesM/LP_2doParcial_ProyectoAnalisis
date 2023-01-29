# Avance: Preprocesamiento y Visualizacion
# Diego Reyes
import pandas as pd
import matplotlib.pyplot as plt
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
    df = dataset[dataset["Pais"]=="Not provided by the user"]
    ordered_df = df.sort_values(by='N_bronce', ascending=True)
    ordered_df.reset_index(inplace=True)
    print("Dataset ordenado por medallas de bronce (y que no proporcionaron su localización en StacKOverflow")
    print(ordered_df.to_string())
    medallasbronce = ordered_df[:10][::-1]
    medallasbronce.reset_index(inplace=True)
    print("\nDataset con Top 10 usuarios con menos medallas de bronce")
    print(medallasbronce.to_string())
    users = []
    medals = []
    for i in range(len(medallasbronce)):
        users.append(medallasbronce.iloc[i]["Nombre"])
        medals.append(medallasbronce.iloc[i]["N_bronce"])
    # Area plot
    plt.figure(figsize=(13, 6))
    plt.style.use('seaborn-darkgrid')
    plt.fill_between(users, medals, color="skyblue", alpha=0.3)
    plt.plot(users, medals, color="skyblue")
    for row in medallasbronce.itertuples():
        plt.text(row.Index, row.N_bronce, row.N_bronce,horizontalalignment='center', verticalalignment='bottom',
                 fontsize=10)
    plt.title("Top 10 usuarios con menos medallas de bronce (y sin info. de ubicación proporcionada)", loc="left")
    plt.xlabel("Usuarios")
    plt.ylabel("# de Medallas")
    plt.show()

def visual3(dataset):
    print("A")


dataset = leer_archivo(archivo)
#Gráfica 1
visual1(dataset)

#Gráfica 2
visual2(dataset)

#Gráfica 3
visual3(dataset)