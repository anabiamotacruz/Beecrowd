_input = input('').split()

codigos = {
    '1':'4.0',
    '2':'4.5',
    '3':'5.0',
    '4':'2.0',
    '5':'1.5'
}

codigo = float(codigos[(_input[0])])
qtd = float(_input[1])

total = codigo*qtd

print(f'Total: R$ {total:.2f}')