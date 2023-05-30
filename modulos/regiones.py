def region(path):
    import csv                      # Importamos csv y platform 
    import platform

    claseslist = []

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\provincias.csv"           # Fix para linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/provincias.csv'

    with open (csvfile, "r", ) as provincias:             # Leemos el archivo clases.csv para la lista de clases
        reader = csv.reader(provincias)
        for row in reader:
            print(row)
            claseslist.append(int(row[1]))
            match int(row[1]):
                case 1:
                   ciudad_de_bsas = [] 
                case 2:
                    bs_as = []
                case 3:
                    catamarca = []
                case 4:
                    cordoba = []
                case 5:
                    corrientes = []
                case 6:
                    chaco = []
                case 7:
                    chubut = []
                case 8:
                    entre_rios = []
                case 9:
                    formosa = []
                case 10:
                    jujuy = []
                case 11:
                    la_pampa = []
                case 12:
                    la_rioja = []
                case 13:
                    mendoza = []
                case 14:
                    misiones = []
                case 15:
                    neuquen = []
                case 16:
                    rio_negro = []
                case 17:
                    salta = []
                case 18: 
                    san_juan = []
                case 19:
                    san_luis = []
                case 20:
                    santa_cruz = []
                case 21:
                    santa_fe = []
                case 22:
                    santiago = []
                case 23:
                    tucuman = []
                case 24:
                    fuego = []