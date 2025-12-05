while True:

    coordenadas = input("Digite as coordenadas: ").split()

    X = int(coordenadas[0])
    Y = int(coordenadas[1])

    if X>0 and Y>0:
        print("primeiro")
    elif X<0 and Y>0:
        print("segundo")
    elif X<0 and Y<0:
        print("terceiro")
    elif X>0 and Y<0:
        print("quarto")
    else:
        break