def csvfilewriter(path, resp):
    import csv
    import platform

 
    if platform.system() == 'Windows':
        csvfile = path + ("\csv\\")             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/'

    if platform.system() == 'Windows':
        csvfile2 = path + ("\csv\\csv_regiones\csv_" )             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile2 = path + '/csv/csv_regiones/csv_'

    csvprov = csvfile + "provincias.csv"

    with open (csvprov, "r", ) as provincias:
        csvreader = csv.reader(provincias)
        for row in csvreader:
            rowactual = str.casefold(row[0])
            rowactual = rowactual.replace(" ", "_")
            csvfilereg = (csvfile2 + rowactual + ".csv")
            
            with open(csvfilereg, "w", ) as provwrite:
                csvwriter = csv.writer(provwrite)
                csvwriter.writerow("test")
            
    
            
    
            

