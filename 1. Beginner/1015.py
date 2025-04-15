_input1 = input('').split()
_input2 = input('').split()

x1 = float(_input1[0])
y1 = float(_input1[1])

x2 = float(_input2[0])
y2 = float(_input2[1])

distancia = (((x2-x1)**2)+((y2-y1)**2))**(1/2)

print(f'{distancia:.4f}')