hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input('').split())

minutos = minuto_final - minuto_inicial
horas = hora_final - hora_inicial

if minutos > 60:

    horas += 1
    minutos -= 60

elif minutos < 0:

    horas -= 1
    minutos += 60

if horas == 0 and (minutos > 0):

    horas = 0

elif horas == 0 and hora_inicial == hora_final:

    horas = 24

elif horas<0:

    horas+= 24

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')