valor = int(input(''))
valor_inicial = valor

notas100 = valor//100
valor -= notas100*100

notas50 = valor//50
valor -= notas50*50

notas20 = valor//20
valor -= notas20*20

notas10 = valor//10
valor -= notas10*10

notas5 = valor//5
valor -= notas5*5

notas2 = valor//2
valor -= notas2*2

notas1 = valor//1
valor -= notas1*1

print(f'{valor_inicial}\n{notas100} nota(s) de R$ 100,00\n{notas50} nota(s) de R$ 50,00\n{notas20} nota(s) de R$ 20,00\n{notas10} nota(s) de R$ 10,00\n{notas5} nota(s) de R$ 5,00\n{notas2} nota(s) de R$ 2,00\n{notas1} nota(s) de R$ 1,00')