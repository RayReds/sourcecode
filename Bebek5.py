n, coklat = input('>').split()
bebek = []
coklat = int(coklat)
for i in range(int(n)):
    b = input('>').split()
    bebek.append((int(b[0]), int(b[1])))
day = 0
while coklat > 0:
    day += 1
    for i in bebek:
        if day % i[0] == 0:
            coklat -= i[1]
            c =
print(day)
int b;
