a = int(input('primer numero     '))
b = int ( input ( 'segundo numero     ' ) )
c = int ( input ( 'tercer numero     ' ) )

suma = 0
n = 2
if a / b > 30:
    x = a / c * b**3
    print(x)
if a / b <= 30:
    while n<=30:
        suma += n**2
        n += 2
        print(suma)