def region2(path, region):
    import platform
    import csv

    votprov = []

    

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\votos.csv"           # Fix para linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/votos.csv'

    with open (csvfile, "r") as votos:
        csvreader = csv.reader(votos)
        for row in csvreader:
            if region == int(row[1]):
                votprov.append(row[3])
                
    return votprov
