import string


class Cesar:
    abc = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, desplazamiento):
        self.desp = desplazamiento
        self.dic = {}
        caracter = string.ascii_lowercase
        for i in range(26):
            self.dic[caracter[i]] = i

    def set_desp(self, desplazamiento):
        self.desp = desplazamiento

    def cifrar(self, texto):
        stri = ''
        a = []
        for x in range(len(texto)):
            a.append(self.dic.get(texto[x]))
        for y in range(len(a)):
            stri += self.abc[(a[y] + self.desp) % 26]
        return stri

    def descifrar(self, texto):
        cifrado_inverso = Cesar(-self.desp)
        texto_clean = cifrado_inverso.cifrar(texto)
        return texto_clean


def cesar_romper(texto):
    cifrado_inverso = Cesar(1)
    for i in range(26):
        cifrado_inverso.set_desp(i)
        texto_break = cifrado_inverso.descifrar(texto)
        print(texto_break)
