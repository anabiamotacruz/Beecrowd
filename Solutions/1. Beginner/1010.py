# -*- coding: utf-8 -*-

input_ = input('')

input_ = input_.split()

peca1 = int(input_[0])

numero1 = int(input_[1])

valor1 = float(input_[2])

input2 = input('')

input2 = input2.split()

peca2 = int(input2[0])

numero2 = int(input2[1])

valor2 = float(input2[2])

peca1 = numero1*valor1

peca2 = numero2*valor2

valortotal = peca1+peca2

print(f'VALOR A PAGAR: R$ {valortotal:.2f}')