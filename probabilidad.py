t = 0
c = 0
for d1 in range(1, 7):
    for d2 in range(1, 7):
        t += 1
        if d1 + d2 > 6:
            c += 1
a = c/36 *100
print(a, '%')