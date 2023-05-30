def contvotos(path):
    import csv
    import platform

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\votos.csv"             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/votos.csv'

    
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0

    with open(csvfile, "r") as archivo:
        reader = csv.reader(archivo, delimiter=",")
        for row in reader:
            clase_votos = int(row[2])
            if clase_votos == 1:
                cont1 = cont1 + 1
            if clase_votos == 2:
                cont2 = cont2 + 1
            if clase_votos == 3:
                cont3 = cont3 + 1
            if clase_votos == 4:
                cont4 = cont4 + 1
    
    return cont1, cont2, cont3, cont4