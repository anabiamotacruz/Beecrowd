def main():

    (A,B,C) = list(map(float, input('').split()))

    perimetro = A+B+C
    area_trapezio = (((A+B)*C)/2)

    if ((A+B)>C) and ((A+C)>B) and ((B+C)>A):

        print(f'Perimetro = {perimetro:.1f}')

    else:

        print(f'Area = {area_trapezio:.1f}')

if (__name__) == '__main__':

    main()