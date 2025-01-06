P = 20201227

table = [0] * P
a = 2959251
b = 4542595

print(pow(b, 7731677, P), pow(7, 7731677*16473833, P))
last = 1
for i in range(P):
    table[last] = i
    if i %10**5 == 0:
        ...
        #print(i)
    last = (last*7)%P


print(table[a], table[b])