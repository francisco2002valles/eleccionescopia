import os
import modulos.menu as menu
import modulos.votos as votos
import modulos.votoswriter as votoswriter

path = os.path.dirname(__file__)

resp = int(menu.menu(path))

cont1, cont2, cont3, cont4, conttotal= votos.contvotos(path)
if resp == 1:
    print(cont1)
elif resp == 2:
    print(cont2)
elif resp == 3:
    print(cont3)
elif resp == 4:
    print(cont4)

votoswriter.csvfilewriter(path, resp)
