def main():

    N = int(input(''))

    horas = N//3600
    N -= 3600*horas

    minutos = N//60
    N -= 60*minutos

    print(f'{horas}:{minutos}:{N}')

if (__name__) == '__main__':

    main()