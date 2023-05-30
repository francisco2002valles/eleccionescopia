def count(path, votprov):
    import csv
    import platform

    desorden = []
    orden = []
    
    def segundo_item(lista):
        return lista[1]

    partid = []
    if platform.system() == 'Windows':
        csvfile = path + "\csv\\partidos.csv"           # Fix para linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/partidos.csv'

    with open (csvfile, "r") as partidos:
        reader = csv.reader(partidos)
        for row in reader:
            partid.append(row[2])


    for item in range(0, len(partid)):
        desorden.append([int(partid[item]),votprov.count(partid[item])])
    
    orden = sorted(desorden, key=segundo_item, reverse=True)
    pos = 0
    temp = len(orden)
    while pos != temp: 
        posact = orden[pos]
        if posact[1] == 0:
            orden.pop(pos)
            temp = temp - 1
        else:
            pos = pos + 1
    print(orden)
    return orden
    
    
    
