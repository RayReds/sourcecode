n, m = input('>').split()
n, m = int(n), int(m)
jenis = [int(i) for i in input('>').split()]
bebek = [int(i) for i in input('>').split()]
total = 0
for b in bebek:
    selisih = []
    [selisih.append(abs(b-i)) for i in jenis]
    total += min(selisih)
print(total)
