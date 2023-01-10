prices = None
toko = []
index = 0
for i in range(int(input('>'))):
    a = input('>').split()
    toko.append((i+1, int(a[0]),int(a[1])))
def Recursive(index):
    global prices
    if toko[index-1][1] == -1:
        if prices:
            if prices[1] >= toko[index-1][2]:
                if prices[0] < index:
                    prices = (index, toko[index-1][2])
        else:
            prices = (index, toko[index-1][2])
        return toko[index-1][2]
    else:
        par = Recursive(toko[index-1][1])+toko[index-1][2]
        if prices:
            if prices[1] >= par:
                if prices[0] < index:
                    prices = (index, par)
        else:
            prices = (index, par)
        return par
for i in toko:
    Recursive(i[0])
print(prices)
