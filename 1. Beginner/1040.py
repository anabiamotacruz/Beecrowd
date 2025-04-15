notas = input('').split()

N1 = float(notas[0])*2
N2 = float(notas[1])*3
N3 = float(notas[2])*4
N4 = float(notas[3])

media = (N1+N2+N3+N4)/10

print(f'Media: {media:.1f}')

if media >= 7:

    print('Aluno aprovado.')

elif 5<=media<=6.9:

    print('Aluno em exame.')

    nota_exame = float(input(''))
    media2 = (media+nota_exame)/2

    print(f'Nota do exame: {nota_exame:.1f}')

    if media2>=5:

        print(f'Aluno aprovado.\nMedia final: {media2:.1f}')

    else:

        print(f'Aluno reprovado.\nMedia final: {media2:.1f}')

else:

    print('Aluno reprovado.')