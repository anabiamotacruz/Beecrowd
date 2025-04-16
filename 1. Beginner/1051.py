def main():

    salario = float(input(''))

    if salario <= 2000:

        print('Isento')

    elif salario <= 3000:

        imposto = (salario-2000)*0.08

        print(f'{imposto:.2f}')

    elif salario <=4500:

        resto = salario-2000
        imposto = ((salario-3000)*0.18)+((salario-2000)*0.08)

        print(f'{imposto:.2f}')

if (__name__) == '__main__':

    main()