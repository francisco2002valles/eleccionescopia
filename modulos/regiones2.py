def region2(region):
    import platform
    import os
    import csv

    votoprov = []

    path = os.path.dirname(__file__)

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\votos.csv"           # Fix para linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/votos.csv'

    with open (csvfile, "r") as votos:
        csvreader = csv.reader(votos)
        for row in csvreader:
            if region == row[1]:
                votoprov.append(row[3])

