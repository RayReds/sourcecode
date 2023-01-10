cases = []

def check(i, p):
    at = 0
    for a in range(len(p)):
        if i[at] == p[a]:
            at+=1
        if at == len(i):
            return len(p)-len(i)
    return "IMPOSSIBLE"
for Z in range(int(input())):
    i = input()
    p = input()
    print(f'Case #{Z+1}: {check(i, p)}')
