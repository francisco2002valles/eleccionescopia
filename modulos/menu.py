def menu(path):
    import csv                      # Importamos csv y platform 
    import platform

    claseslist = []                   # Creamos una lista para todos las clases

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\clases.csv"           # Fix para linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/clases.csv'

    with open (csvfile, "r", ) as partidos:             # Leemos el archivo clases.csv para la lista de clases
        reader = csv.reader(partidos)
        for row in reader:
            print(row)
            claseslist.append(int(row[2]))
    
    print("Seleccione que resultado desea ver: ")
    valido = False
    while valido != True:                           # Chequeamos que el valor sea valido
        try:
            resp = int(input(": "))               # Chequeamos que el valor sea un numero
        except: 
            valido = False
        try:
            claseslist.index(resp)                # Buscamos el valor en la lista de clases
            valido = True
        except:
            valido = False
            print("Valor no valido")                # si no lo encuentra tira un error, usamos esto para definirlo como no valido

    return resp