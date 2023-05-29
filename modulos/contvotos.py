import csv                      # Importamos csv y platform
import platform
contador = [0, 0, 0, 0]
if platform.system() == 'Windows':
    filename = ".\csv\votos.csv"           # Fix para linux
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
print(f"Votos Presidente y vicepresidente: {contador[0]}")
print(f"Votos Gobernador y vicegobernador: {contador[1]}")
print(f"Votos Senadores: {contador[2]}")
print(f"Votos Diputados: {contador[3]}")
