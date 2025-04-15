def saida(idade_pessoa):

    x = idade_pessoa

    anos = x//365
    x -= anos*365

    meses = x//30
    x -= meses*30

    print(f'{anos} ano(s)\n{meses} mes(es)\n{x} dia(s)')

def main():

    idade = int(input(''))

    saida(idade)

if (__name__) == '__main__':

    main()