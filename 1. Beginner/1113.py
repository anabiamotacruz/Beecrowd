while(True):
    valores = input().split()

    X = int(valores[0])
    Y = int(valores[1])

    if (X>Y):
        print("Decrescente")
    elif (Y>X):
        print("Crescente")
    else:
        break