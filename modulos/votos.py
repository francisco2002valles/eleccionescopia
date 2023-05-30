def contvotos(path):
    import csv
    import platform

    if platform.system() == 'Windows':
        csvfile = path + ".\csv\\votos.csv"             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/votos.csv'

    contblanco = 0 
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    conttotal = 0
    prov1 = 0
    prov2 = 0
    prov3 = 0
    prov4 = 0
    prov5 = 0
    prov6 = 0
    prov7 = 0
    prov8 = 0
    prov9 = 0
    prov10 = 0
    prov11 = 0
    prov12 = 0
    prov13 = 0
    prov14 = 0
    prov15 = 0
    prov16 = 0
    prov17 = 0
    prov18 = 0
    prov19 = 0
    prov20 = 0
    prov21 = 0
    prov22 = 0
    prov23 = 0
    prov24 = 0

    with open(csvfile, "r") as archivo:
        reader = csv.reader(archivo, delimiter=",")
        for row in reader:
            match int(row[1]):
            case 1:
                prov1 = prov1 + 1
            case 2:
                prov2 = prov2 + 1
            case 3:
                prov3 = prov3 + 1
            case 4:
                prov4 = prov4 + 1
            case 5:
                prov5 = prov5 + 1
            case 6:
                prov6 = prov6 + 1
            case 7:
                prov7 = prov7 + 1
            case 8:
                prov8 = prov8 + 1
            case 9:
                prov9 = prov9 + 1
            case 10:
                prov10 = prov10 + 1
            case 11:
                prov11 = prov11 + 1
            case 12:
                prov12 = prov12 + 1
            case 13:
                prov13 = prov13 + 1
            case 14:
                prov14 = prov14 + 1
            case 15:
                prov15 = prov15 + 1
            case 16:
                prov16 = prov16 + 1
            case 17:
                prov17 = prov17 + 1
            case 18:
                prov18 = prov18 + 1
            case 19:
                prov19 = prov19 + 1
            case 20:
                prov20 = prov20 + 1
            case 21:
                prov21 = prov21 + 1
            case 22:
                prov22 = prov22 + 1
            case 23:
                prov23 = prov23 + 1
            case 24:
                prov24 = prov24 + 1
            

    with open(csvfile, "r") as archivo:
        reader = csv.reader(archivo, delimiter=",")
        for row in reader:
            clase_votosblanco = int(row[3])
            if clase_votosblanco == 000:
                contblanco = contblanco + 1

    with open(csvfile, "r") as archivo:
        reader = csv.reader(archivo, delimiter=",")
        for row in reader:
            clase_votos = int(row[2])
            conttotal = conttotal + 1
            if clase_votos == 1:
                cont1 = cont1 + 1
            if clase_votos == 2:
                cont2 = cont2 + 1
            if clase_votos == 3:
                cont3 = cont3 + 1
            if clase_votos == 4:
                cont4 = cont4 + 1
    
    return cont1, cont2, cont3, cont4, conttotal, contblanco