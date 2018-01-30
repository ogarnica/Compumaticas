class Complejos:
    def __init__(self, real, imaginario):
        self.r = real
        self.i = imaginario

    def suma(self, other):
        sum_real = self.r + other.r
        sum_ima = self.i + other.i
        return ('(%d, %d)' %(float(sum_real), float(sum_ima)))

    def resta(self, other):
        res_real = self.r - other.r
        res_ima = self.i - other.i
        return ('(%d, %d)' % (float(res_real), float(res_ima)))

    def multiplicacion(self, other):
        mult_real = self.r * other.r - self.i * other.i
        mult_ima = self.r * other.i + self.i * other.r
        return ('(%d, %d)' % (float(mult_real), float(mult_ima)))

    def __repr__(self):
        return (str(self.r)+'+'+str(self.i)+'i')

    def __add__(self, other):
        return (self.suma(other))

    def __sub__(self, other):
        return (self.resta(other))

    def __mul__(self, other):
        return (self.multiplicacion(other))


# x = Complejos(3.0, 4.0)
# y = Complejos(3.0, 7.0)
# x.suma(y)
# x + y
# Complejos.suma(x, y)