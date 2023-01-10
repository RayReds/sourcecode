import math
def findFactor(num):
    a = 0
    for i in range(1,int(math.sqrt(num))+1):
        if num%i == 0:
            a+= isPalindrome(i)
            if i*i != num:
                a+=isPalindrome(num//i)
    return a
def isPalindrome(n):
    normal = str(n)
    reverse = normal[::-1]
    return normal == reverse
for i in range(int(input())):
    num = int(input())
    print(f'Case #{i+1}: {findFactor(num)}')
