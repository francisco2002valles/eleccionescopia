def csvfilewriter(path, resp):
    import csv
    import platform

    header1 = ["ELECCIONES GENERALES 2023"]

    if platform.system() == 'Windows':
        csvfile = path + ("\csv\\")             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/'

    if resp == 1:
        cat = "presidente_"
    if resp == 2:
        cat = "gobernador_"
    if resp == 3:
        cat = "diputado_"
    if resp == 4:
        cat = "senadores_"

    if platform.system() == 'Windows':
        csvfile2 = path + ("\csv\\csv_regiones\csv_" + cat)             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile2 = path + '/csv/csv_regiones/csv_' + cat

    csvprov = csvfile + "provincias.csv"

    


    with open (csvprov, "r", ) as provincias:
        csvreader = csv.reader(provincias)
        for row in csvreader:
            rowactual = str.casefold(row[0])
            rowactual = rowactual.replace(" ", "_")
            csvfilereg = (csvfile2 + rowactual + ".csv")
            
            with open(csvfilereg, "w", ) as provwrite:
                csvwriter = csv.writer(provwrite)
                csvwriter.writerow([row[0]])
                csvwriter.writerow(header1)
            
    
            
    
            

