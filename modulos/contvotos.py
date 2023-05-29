import csv                      # Importamos csv y platform
import platform
contador = [0, 0, 0, 0]
if platform.system() == 'Windows':
    filename = path + "\csv\\partidos.csv"           # Fix para linux
elif platform.system() == 'Linux':
    filename = '../csv/votos.csv'

with open(filename, 'r') as votos:
    for voto in votos:
        match int(voto[2]):
            case 1:
                contador[0] += 1
            case 2:
                contador[1] += 1
            case 3:
                contador[2] += 1
            case 4:
                contador[3] += 1
print(contador)
