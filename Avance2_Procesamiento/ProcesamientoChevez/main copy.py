# Lectura del archivo
def leerArchivo(filename):
    file = open(filename, "r")
    file.readline()
    cont = 0
    for linea in file:
        numero, empresa, ciudades , habilidades = linea.strip().split(",")
        # print("Numero: {numero}, empresa: {empresa}, ciudades: {ciudades}, habilidades: {habilidades}")
        if cont == 5:
            break


leerArchivo("/dataset-kchevez.csv")