def main():

    num_positivo = 0

    for i in range(5):

        num = int(input(''))

        if (num%2)==0:

            num_positivo += 1

    print(f'{num_positivo} valores pares')

if (__name__) == '__main__':

    main()