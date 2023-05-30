def formato(path, orden):
    import platform
    import csv
    if platform.system() == 'Windows':
        csvfile = path + "\csv\\partidos.csv"           # Fix para linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/partidos.csv'
    temp = []
    final = []
    nombre = ""
    votosblanco = 0
    votostotal = 0
    def primer_item(lista):
        return lista[0]

    def segundo_item(lista):
        return lista[1]    
    for item in range(0, len(orden)):
        temp.append(primer_item(orden[item]))
        
        with open (csvfile, "r") as partidos:
            reader = csv.reader(partidos)
            for row in reader:
                if primer_item(orden[item]) == int(row[2]):
                    nombre = row[0]
            
        if primer_item(orden[item]) == 0:
            temp = []
            votosblanco = segundo_item(orden[item])
        if primer_item(orden[item]) != 0:
            temp.append(nombre)
            temp.append(segundo_item(orden[item]))    
            final.append(temp)

        votostotal = votostotal + segundo_item(orden[item])
        
        temp = []

    return final, votosblanco, votostotal

    
    


        