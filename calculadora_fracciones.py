num1 = int(input('numerador 1: '))
den1 = int(input('denominador 1: '))
operacion = input('operacion: ')
num2 = int(input('numerador 2: '))
den2 = int(input('denominador 2: '))

if operacion == '+':
    print((num1 * den2) + (num2 * den1), '/', den1 * den2)
elif operacion == '-':
    print((num1 * den2) - (num2 * den1), '/', den1 * den2)
elif operacion == '*':
    print(num1 * num2, '/', den1 *den2)
elif operacion == '/':
    print(num1 * den2, '/', num2 * den1)