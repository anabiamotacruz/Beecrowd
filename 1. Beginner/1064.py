positivo = []
soma = 0

for i in range(6):

    num = float(input(''))

    if num>=0:

        positivo.append(num)
        soma+=num

media = soma/len(positivo)

print(f'{len(positivo)} valores positivos\n{media:.1f}')