# -*- coding: utf-8 -*-

input_ = input('')

input_ = input_.split()

A = float(input_[0])

B = float(input_[1])

C = float(input_[2])

triangulo=(A*C)/2

circulo=(3.14159)*(C**2)

trapezio=((A+B)/2)*C

quadrado=B*B

retangulo=A*B

print(f'TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}')