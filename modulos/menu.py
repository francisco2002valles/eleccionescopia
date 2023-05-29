def menu():
    print("Que tipo de resultados electorales desea ver?")
    print("1- Presidente y Vicepresidente ")
    print("2- Gobernador y Vicegobernador ")
    print("3- Senadores")
    print("4- Diputados")

    val = False

    while val != True:
        try:
            cat = str(input(": ")) 
            if cat != "1" and cat != "2" and cat != "3" and cat != "4":             # Validamos la categoria
                val = False
                print("Valor no valido")
            else:
                val = True
        except ValueError:
            print("Valor no valido")
            val = False
    return cat