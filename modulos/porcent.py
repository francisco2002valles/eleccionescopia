def porcent():
    import os
    import platform
    import modulos.votos as votos

    path = os.path.dirname(__file__)

    cont1, cont2, cont3, cont4, conttotal, contblanco = votos.contvotos(path)

    porcent1 = (cont1 * 100)/conttotal
    porcent2 = (cont2 * 100)/conttotal
    porcent3 = (cont3 * 100)/conttotal
    porcent4 = (cont4 * 100)/conttotal
    porcentblanco = (contblanco * 100)/conttotal

    return porcent1, porcent2, porcent3, porcent4, porcentblanco
