def main():

    num = int(input(''))

    if num%2==0:

        for i in range(12):

            if (num+i)%2!=0:

                print(num+i)

    else:

        for i in range(11):

            if (num+i)%2!=0:

                print(num+i)

if (__name__) == '__main__':

    main()