x = int(input(''))
y = int(input(''))

soma = 0

if y>=x:
    for i in range(x,y):

        if i%2!=0:

            soma+=i

else:

    for i in range(x-1,y,-1):

        if i%2!=0:

            soma+=i

print(soma)