def csvfilewriter(path, resp):
    import csv
    import platform
    import modulos.regiones2 as reg

    votprov = []

    if platform.system() == 'Windows':
        csvfile = path + ("\csv\\")             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/'

    if resp == 1:
        cat = "presidente"
    if resp == 2:
        cat = "gobernador"
    if resp == 3:
        cat = "diputado"
    if resp == 4:
        cat = "senadores"

    if platform.system() == 'Windows':
        csvfile2 = path + f"\csv\\csv_regiones\{cat}\csv_"             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile2 = path + f'/csv/csv_regiones/{cat}/csv_'

    csvprov = csvfile + "provincias.csv"

    header1 = ["ELECCIONES GENERALES 2023"]
    body1 = [f"Categoria: {cat}"]
    body2 = ["N° De lista", "Partido politico", "Votos", "Porcentaje %"]


    with open (csvprov, "r", ) as provincias:
        csvreader = csv.reader(provincias)
        for row in csvreader:
            rowactual = str.casefold(row[0])
            rowactual = rowactual.replace(" ", "_")
            csvfilereg = (csvfile2 + rowactual + f"{cat}.csv")
            
            with open(csvfilereg, "w", ) as provwrite:
                csvwriter = csv.writer(provwrite)
                csvwriter.writerow([row[0]])
                print(int(row[1]))
                votprov = reg.region2(path,int(row[1]))
                print (votprov)
                csvwriter.writerow(header1)
                csvwriter.writerow(body1)
                csvwriter.writerow(body2)
                csvwriter.writerow(votprov)
                

            
    
            
    
            

