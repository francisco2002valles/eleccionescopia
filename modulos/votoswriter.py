def csvfilewriter(path, resp):
    import csv
    import platform

 
    if platform.system() == 'Windows':
        csvfile = path + (f"\csv\\")             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/'

    if platform.system() == 'Windows':
        csvfile2 = path + (f"\csv\\csv_regiones\csv_" )             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile2 = path + '/csv/csv_regiones/csv_'

    csvprov = csvfile + "provincias.csv"
    

    with open (csvprov, "r") as provincias:
        csvreader = csv.reader(provincias)
        for row in provincias:
            rowactual = []
            rowactual.append(row)
            csvfilereg = (csvfile2 + rowactual[0] + ".csv")
            
            with open(csvfilereg, "w", ) as provwrite:
                csvwriter = csv.writer(provwrite)
                csvwriter.writerow("test")
            
    
            
    
            

