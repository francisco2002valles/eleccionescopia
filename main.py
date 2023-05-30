import os
import modulos.menu as menu
import modulos.votos as votos
import modulos.votoswriter as votoswriter

import platform

path = os.path.dirname(__file__)

resp = int(menu.menu(path))

cont1, cont2, cont3, cont4, conttotal= votos.contvotos(path)
if resp == 1:
    print(cont1)
    cat = "presidente"
elif resp == 2:
    print(cont2)
    cat = "gobernador"
elif resp == 3:
    print(cont3)
    cat = "diputados"
elif resp == 4:
    print(cont4)
    cat = "senadores"

if platform.system() == 'Windows':
    dirloc = path + f"\csv\\csv_regiones\\{cat}"           # Fix para linux
elif platform.system() == 'Linux':
    dirloc = path + f'/csv/csv_regiones/{cat}'

if platform.system() == 'Windows':
    dirloc1 = path + f"\csv\\csv_regiones"           # Fix para linux
elif platform.system() == 'Linux':
    dirloc1 = path + f'/csv/csv_regiones'

try:
    os.mkdir(dirloc1, mode=0o777)
    
except:
    print("")

try:
    os.mkdir(dirloc, mode=0o777)
    
    votoswriter.csvfilewriter(path, resp)

except:
    
    votoswriter.csvfilewriter(path, resp)





