codigo = {
   "a": ".-",
   "b": "-...",
   "c": "-.-.",
   "d": "-..",
   "e": ".",
   "f": "..-.",
   "g": "--.",
   "h": "....",
   "i": "..",
   "j": ".---",
   "k": "-.-",
   "l": ".-..",
   "m": "--",
   "n": "-.",
   "ñ": "--.--",
   "o": "---",
   "p": ".--.",
   "q": "--.-",
   "r": ".-.",
   "s": "...",
   "t": "-",
   "u": "..-",
   "v": "...-",
   "w": ".--",
   "x": "-..-",
   "y": "-.--",
   "z": "--..",
   "0": ".....",
   "1": "....-",
   "2": "...--",
   "3": "..---",
   "4": ".----",
   "5": "-----",
   "6": "----.",
   "7": "---..",
   "8": "--...",
   "9": "-....",
   " ": " "}

while True:
    texto = input('Dime un texto que quieras traducir: ')
    
    for x in range(len(texto)):
        print(codigo[texto[x]])
