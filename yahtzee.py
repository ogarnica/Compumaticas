import random as r

trio = 0
poker = 0
full = 0
esc_pe = 0
esc_gr = 0
rigole = 0
yahtzee = 0
nada = 0
veces = 100000000
por_cien = veces/100

class Dados:

    def __init__(self, d1, d2, d3, d4, d5):
        self.dados = [d1, d2, d3, d4, d5]

    def hay_full(self):
        for z in range(1, 7):
            if self.dados.count(z) == 3:
                if self.dados.count((z + 1) % 6) == 2 or self.dados.count((z + 2) % 6) == 2 or self.dados.count(
                        (z + 3) % 6) == 2 or self.dados.count((z + 4) % 6) == 2 or self.dados.count((z + 5) % 6) == 2:
                    return True

    def hay_trio(self):
        if self.hay_full() != True:
            for x in range(1, 7):
                if self.dados.count(x) == 3:
                    return True

    def hay_yahtzee(self):
        for d in range(1, 7):
            if self.dados.count(d) == 5:
                return True

    def hay_rigole(self):
        if self.hay_yahtzee() != True:
            for c in range(1, 7):
                if self.dados.count(c) == 4:
                    if 7-c in self.dados:
                        return True

    def hay_poker(self):
        if self.hay_rigole() != True:
            for y in range(1, 7):
                if self.dados.count(y) == 4:
                    return True

    def hay_esc_grand(self):
        for b in range(1, 3):
            if b in self.dados:
                if b+1 in self.dados:
                    if b+2 in self.dados:
                        if b+3 in self.dados:
                            if b+4 in self.dados:
                                return True

    def hay_esc_peq(self):
        if self.hay_esc_grand() != True:
            for a in range(1, 4):
                if a in self.dados:
                    if a+1 in self.dados:
                        if a+2 in self.dados:
                            if a+3 in self.dados:
                                return True

for n in range(veces):

    m = Dados(r.randint(1, 6), r.randint(1, 6), r.randint(1, 6), r.randint(1, 6), r.randint(1, 6))

    if m.hay_trio():
        trio += 1
        print('Tienes un trio')
    if m.hay_poker():
        poker += 1
        print('Tienes un poker')
    if m.hay_full():
        full += 1
        print('Tienes un full')
    if m.hay_esc_peq():
        esc_pe += 1
        print('Tienes una escalera pequena')
    if m.hay_esc_grand():
        esc_gr += 1
        print('Tienes una escalera grande')
    if m.hay_rigole():
        rigole += 1
        print('Tienes un rigole')
    if m.hay_yahtzee():
        yahtzee += 1
        print('Tienes un yahtzee')

    if not m.hay_trio() and not m.hay_poker() and not m.hay_full() and \
            not m.hay_esc_peq() and not m.hay_esc_grand() and \
            not m.hay_rigole() and not m.hay_yahtzee():
        nada += 1
        print('No te ha salido nada. Jajaja')

print('Trios: ', trio/por_cien, ' %')
print('Poker: ', poker/por_cien, ' %')
print('Full: ', full/por_cien, ' %')
print('Esc pequena: ', esc_pe/por_cien, ' %')
print('Esc grande: ', esc_gr/por_cien, ' %')
print('Rigole: ', rigole/por_cien, ' %')
print('Yahtzee: ', yahtzee/por_cien, ' %')
print('Nada: ', nada/por_cien, ' %')