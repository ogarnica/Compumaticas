dividendo = int(input('dividendo: '))
divisor = int(input('divisor: '))
cociente = dividendo // divisor
resto = dividendo % divisor
for x in range(divisor):
    print('--  '+cociente*' o')
print('--resto--  '+resto*' o')
