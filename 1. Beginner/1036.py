valores = input('').split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

delta = (((B**2)-(4*A*C))**(0.5))

if ((B**2)-(4*A*C))>=0 and A!=0:

    R1 = ((-B)+((delta)))/(2*A)
    R2 = ((-B)-((delta)))/(2*A)

    print(f'R1 = {R1:.5f}\nR2 = {R2:.5f}')

else:

    print('Impossivel calcular')