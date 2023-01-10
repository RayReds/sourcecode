
def isPalindrome(n):
    normal = str(n)
    reverse = normal[::-1]
    return normal == reverse
num = input()
num = num.split(', ')
a = []
for i in num:
    if isPalindrome(i):
        a.append(i)
print(a)
print(len(a))
