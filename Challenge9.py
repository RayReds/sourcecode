#Problem at https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997


def find(n):
    add = 9 - (int(n)%9)
    if int(n)%9 == 0:
        return n[0]+'0'+n[1:]
    for i in range(len(n)):
        if int(n[i]) > add:
            a = n[:i]+str(add)+n[i:]
            return a
    return n+str(add)
for i in range(int(input())):
    num = input()
    print(f'Case #{i+1}: {find(num)}')
