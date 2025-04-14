# -*- coding: utf-8 -*-

input_ = input('')

input_ = input_.split()

a = int(input_[0])

b = int(input_[1])

c = int(input_[2])

maior = (a+b+abs(a-b))/2

if maior==a:

    maior=(a+c+abs(a-c))/2

else:

    maior=(c+b+abs(c-b))/2
    
print(f'{maior:.0f} eh o maior')