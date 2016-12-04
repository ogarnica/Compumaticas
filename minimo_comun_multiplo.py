#nu1=int(input('aaa'))
#nu2=int(input('bbb'))
def minimo (nu1, nu2):
    if nu1>nu2:
        mayor=nu1
        menor=nu2
    elif nu1<nu2:
        mayor=nu2
        menor=nu1

    if mayor%menor==0:
        print('el m.c.m. de ',nu1,' y ',nu2,' es ',mayor)
    for x in range(1, menor+1):
        if mayor%menor!=0:
            m=mayor*x
            print(m)
            if m%menor==0:
                print('los multiplos son', m)
