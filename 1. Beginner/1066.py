def main():

    val_par = 0
    val_impar = 0
    val_pos = 0
    val_neg = 0

    for i in range(5):

        num = int(input(''))

        if num >0:

            val_pos += 1

        elif num<0:

            val_neg += 1

        if (num%2)==0:

            val_par += 1

        else:

            val_impar += 1

    print(f'{val_par} valor(es) par(es)\n{val_impar} valor(es) impar(es)\n{val_pos} valor(es) positivo(s)\n{val_neg} valor(es) negativo(s)')

if (__name__) == '__main__':

    main()