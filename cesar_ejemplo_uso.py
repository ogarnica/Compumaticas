from cesar import *


cifrado1 = Cesar(28)
texto_cifrado = cifrado1.cifrar('hola')
print(texto_cifrado)

texto_descifrado = cifrado1.descifrar(texto_cifrado)
print(texto_cifrado + '-->' + texto_descifrado)

cesar_romper('alsdfalsk')
