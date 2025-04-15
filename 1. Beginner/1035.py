_input = (input('')).split()

A = int(_input[0])
B = int(_input[1])
C = int(_input[2])
D = int(_input[3])

if (B>C) and (D>A) and ((C+D)>(A+B)) and (C>0) and (D>0) and (A%2==0):

    print('Valores aceitos')

else:

    print('Valores nao aceitos')