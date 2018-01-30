import turtle as t

def numeros():
    num_num = int(input('Maximo: '))
    a = [1,1]
    for i in range(100):
        a.append(a[i] + a[i + 1])
        if a[i+1] > num_num:
            a.remove(a[-1])
            a.remove(a[-1])
            print(a)
            exit()

#numeros()

def espiral():
    print(len(a))
    for x in range(len(a)):
        t.fd((a[x])*10)
        t.rt(90)
    t.done()
    exit()


num_num = int(input('Maximo: '))
a = [1,1]
for i in range(10000):
    a.append(a[i] + a[i + 1])
    if a[i+1] > num_num:
        a.remove(a[-1])
        a.remove(a[-1])
        print(a)
        espiral()

