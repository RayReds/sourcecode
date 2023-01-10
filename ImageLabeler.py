#Problems at : https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76e11
def getMedian(s):
    s.sort()
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return (s[mid] + s[mid-1]) / 2
    else:
        return s[mid]
for cases in range(int(input())):
    split = input().split()
    numCategories = int(split[1])
    categories = []
    regions = [int(i) for i in input().split()]
    min = (None, max(regions)+1)
    for i in range(numCategories):
        top = max(regions)
        if min[1] > top:
            min = (len(categories), top)
        categories.append([top])
        regions.pop(regions.index(top))
    categories[min[0]] += regions
    #print(categories)
    total = 0
    for i in categories:
        total += getMedian(i)
    print(f'Case #{cases+1}: {float(total)}')
