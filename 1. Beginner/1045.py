def main():

    nums = list(map(float, input('').split()))

    nums.sort(key=float, reverse=True)

    A = nums[0]
    B = nums[1]
    C = nums[2]

    if A>=(B+C):

        print('NAO FORMA TRIANGULO')

    else:

        if (A**2)==((B**2)+(C**2)):

            print('TRIANGULO RETANGULO')

        if (A**2)>((B**2)+(C**2)):

            print('TRIANGULO OBTUSANGULO')

        if (A**2)<((B**2)+(C**2)):

            print('TRIANGULO ACUTANGULO')

        if A==B and A==C:

            print('TRIANGULO EQUILATERO')

        if ((A==C) and (A!=B)) or ((A==B) and (A!=C)) or ((B==C) and (B!=A)):

            print('TRIANGULO ISOSCELES')

if (__name__) == '__main__':

    main()