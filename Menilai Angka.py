nums = []
for i in range(int(input('> '))):
    nums.append(int(input('> ')))

def gcd(a, b):
    print(a, b)
    if a == 0:
        return b
    else:
        return gcd(b%a, a)
b = 1
gcdS = None
while True:
    print(b, gcdS)
    if b == len(nums):
        break
    elif gcdS == None:
        gcdS = gcd(nums[0], nums[b])
        b += 1
    else:
        print(gcdS)
        gcdS = gcd(nums[b], gcdS)
        b += 1
print(gcdS)
