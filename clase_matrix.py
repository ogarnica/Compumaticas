import random

class Matrix:
    def __init__(self, m, n, rnd=True):
        self.m = m
        self.n = n
        self.M = []
        for fila in range(m):
            f = [ random.randint(-5,5) for col in range(n) ]
            self.M.append(f)
    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            return False
        else:
            z = Matrix(self.m, self.n)
            for i in range(self.m):
                for j in range(self.n):
                    z.M[i][j] = self.M[i][j] + other.M[i][j]
            return z

    def __sub__(self, other):
        if self.m != other.m or self.n != other.n:
            return False
        else:
            z = Matrix(self.m, self.n)
            for i in range(self.m):
                for j in range(self.n):
                    z.M[i][j] = self.M[i][j] - other.M[i][j]
            return z

    def __mul__(self, other):
        if self.n != other.m:
            return False
        else:
            z = Matrix(self.m, other.n)
            for i in range(self.m):
                for j in range(other.n):
                    cont = 0
                    for k in range(self.n):
                        cont += self.M[i][k] * other.M[k][j]
                    z.M[i][j] = cont
            return z

    def __repr__(self):
        s = ''
        for fila in self.M:
            s += str(fila) + '\n'
        return s[:-1]

    def __div__(self):
        num = int(input('num: '))
        for a in range(self.n):
            for b in range(self.m):
                self.M = self.M[a][b] / num