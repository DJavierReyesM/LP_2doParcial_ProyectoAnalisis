import pandas as pd

# Lectura del archivo
def leerArchivo(filename):
    dataFrame = pd.read_csv(filename, encoding='utf8')
    dictCiudades = {}
    dictHabilidadesDuras = {}
    for linea in dataFrame.itertuples():
        # print(linea.ciudades)
        ciudades = linea.ciudades.strip().split(";")
        for ciudad in ciudades:
            if(ciudad not in dictCiudades):
                dictCiudades[ciudad] = 1
            else:
                dictCiudades[ciudad] += 1

        habilidadesDuras = linea.habilidades.strip().split(";")
        for habilidad in habilidadesDuras:
            if(habilidad not in dictHabilidadesDuras):
                dictHabilidadesDuras[habilidad] = 1
            else:
                dictHabilidadesDuras[habilidad] += 1
        

    print("Diccionario ciudades final: ")
    print(dictCiudades)
    print("Diccionario habilidades duras final: ")
    print(dictHabilidadesDuras)


leerArchivo("dataset-kchevez.csv")