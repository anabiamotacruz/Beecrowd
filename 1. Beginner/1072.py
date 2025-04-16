def main():

    N = int(input(''))

    lista = []

    dentro = 0
    out = 0

    for i in range(N):

        num = int(input(''))

        lista.append(num)

    for i in lista:

        if 10<=i<=20:

            dentro += 1

        else:

            out += 1

    print(f'{dentro} in\n{out} out')

if (__name__) == '__main__':

    main()