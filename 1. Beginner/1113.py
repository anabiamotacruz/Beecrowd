valores = input("Digite os numeros: ").split()

X = int(valores[0])
Y = int(valores[1])

if (X>Y):
    print("Decrescente")
elif (Y>X):
    print("Crescente")