def csvfilewriter(path, resp):
    import csv
    import platform

    if platform.system() == 'Windows':
        csvfile = path + "\csv\csv_regiones\\votos.csv"             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/csv_regiones/votos.csv'

    with open (csvfile, "r") as votos:
        csvreader = csv.reader(votos)
        for row in csvreader

