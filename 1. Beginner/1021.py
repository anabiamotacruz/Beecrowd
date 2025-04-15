def moedas_notas(valor):

    x = int(valor*100)

    notas100 = x//10000
    x -= 10000*notas100

    notas50 = x//5000
    x -= 5000*notas50

    notas20 = x//2000
    x -= 2000*notas20

    notas10 = x//1000
    x -= 1000*notas10

    notas5 = x//500
    x -= 500*notas5

    notas2 = x//200
    x -= 200*notas2

    moedas1 = x//100
    x -= moedas1*100

    moedas05 = x//50
    x -= moedas05*50

    moedas025 = x//25
    x -= moedas025*25

    moedas01 = x//10
    x -= moedas01*10

    moedas005 = x//5
    x -= moedas005*5

    moedas001 = x//1
    x -= moedas001*1

    print(f'NOTAS:\n{notas100:.0f} nota(s) de R$ 100.00\n{notas50:.0f} nota(s) de R$ 50.00\n{notas20:.0f} nota(s) de R$ 20.00\n{notas10:.0f} nota(s) de R$ 10.00\n{notas5:.0f} nota(s) de R$ 5.00\n{notas2:.0f} nota(s) de R$ 2.00')
    print(f'MOEDAS:\n{moedas1:.0f} moeda(s) de R$ 1.00\n{moedas05:.0f} moeda(s) de R$ 0.50\n{moedas025:.0f} moeda(s) de R$ 0.25\n{moedas01:.0f} moeda(s) de R$ 0.10\n{moedas005:.0f} moeda(s) de R$ 0.05\n{moedas001:.0f} moeda(s) de R$ 0.01')

def main():

    N = float(input(''))

    moedas_notas(N)

if (__name__) == '__main__':

    main()