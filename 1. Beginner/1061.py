dia1 = input('')
dia1 = dia1[4:]
horas1,minutos1,segundos1 = map(int, input('').split(' : '))
dia2 = input('')
dia2 = dia2[4:]
horas2,minutos2,segundos2 = map(int, input('').split(' : '))

dias = dia2-dia1

horas = horas2-horas1

minutos = minutos2-minutos1

segundos = segundos2-segundos1

if horas==0:

    dias+=1

if minutos >= 60:

    horas+=1

    minutos -= 60

if segundos >= 60:

    minutos+=1

    segundos -= 60