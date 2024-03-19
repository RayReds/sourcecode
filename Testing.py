def hijau(x, y):
    if x < y:
        x = x+y
        y = x-y
        x = x-y
    if y == 0:
        return x
    return hijau(x-y, y)
def merah(q, w, e, r):
    if q < w:
        return 0
    return hijau(q, e)+merah(q-r, w, e, r)
def biru(n):
    ans = 0
    ans += merah(n, 1, n, 1)
    ans -= merah(2 * n, 2, n, 2)
    return ans * 3
print(biru(69))
        