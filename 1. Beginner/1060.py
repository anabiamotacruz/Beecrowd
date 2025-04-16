def main():

    nums = []
    num_positivo = 0

    for i in range(6):

        num = float(input(''))

        nums.append(num)

    for i in nums:

        if i>0:

            num_positivo += 1

    print(f'{num_positivo} valores positivos')

if (__name__) == '__main__':

    main()