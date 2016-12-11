#   *
#  * *
# * * *
#* * * *

altura = int(input('di la altura'))
estrella = '*'
stars = 1
for x in range(altura, 0, -1):
    print(x*' ',estrella*stars)
    stars += 2
