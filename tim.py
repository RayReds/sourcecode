cases = []
for i in range(int(input())):
    i = input()
    p = input()
    cases.append((p, i))
def check(p, i):
    if len(i) >= len(p):
        return 'IMPOSSIBLE'
    li1 = list(i)
    li2 = list(p)
    check = []
    for i in range(len(li1)):
        for a in range(len(li2)):
            if li1[i] == li2[0]:
                check.append(li2[0])
                li2.pop(0)
                break
            li2.pop(0)
    if li1 == check:
        return len(p)-len(check)
    else:
        return 'IMPOSSIBLE'
for i in cases:
    print(f'Case #{cases.index(i)+1}: {check(i[0], i[1])}')
