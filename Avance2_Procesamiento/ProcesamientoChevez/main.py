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
    # print(dictCiudades)
    print("Diccionario habilidades duras final: ")
    # print(dictHabilidadesDuras)
    # imprimirDiccionario(dictCiudades, "Tabla de frecuencia de ciudades")
    # imprimirDiccionario(dictHabilidadesDuras, "Tabla de frecuencia de Habilidades duras")
    dataFrameCiudades = pd.DataFrame(list(dictCiudades.items()))
    dataFrameCiudades.columns = ["CIUDAD", "FRECUENCIA"]
    dataFrameCiudades.sort_values(by=["FRECUENCIA"])

    dataFrameHabilidades = pd.DataFrame(list(dictHabilidadesDuras.items()))
    dataFrameHabilidades.columns = ["HABILIDAD", "FRECUENCIA"]
    dataFrameHabilidades.sort_values("FRECUENCIA")
    
    dataFrameCiudades.drop_duplicates()
    print(dataFrameCiudades)
    dataFrameHabilidades.drop_duplicates()
    print(dataFrameHabilidades)


def imprimirDiccionario(dic, titulo):
    print(f"----------------- {titulo} -----------------")
    for clave,valor in dic.items():
        print(f"{clave}: {valor}")



leerArchivo("dataset-kchevez.csv")