def main():

    (t1,t2,t3,t4) = map(int, input('').split())

    tomadas = t1+(t2-1)+(t3-1)+(t4-1)

    print(f'{tomadas:.0f}')

if (__name__) == '__main__':

    main()