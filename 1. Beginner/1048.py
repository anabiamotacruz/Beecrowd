def main():

    salario = float(input(''))

    if salario<=400.00:

        novo_salario = salario+(salario*0.15)
        reajuste = novo_salario-salario

        print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 15 %')

    elif salario<=800.00:

        novo_salario = salario+(salario*0.12)
        reajuste = novo_salario-salario

        print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 12 %')

    elif salario<=1200.00:

        novo_salario = salario+(salario*0.1)
        reajuste = novo_salario-salario

        print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 10 %')

    elif salario<=2000.00:

        novo_salario = salario+(salario*0.07)
        reajuste = novo_salario-salario

        print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 7 %')

    else:

        novo_salario = salario+(salario*0.04)
        reajuste = novo_salario-salario

        print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 4 %')

if (__name__) == '__main__':

    main()