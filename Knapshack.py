capacity = 10

weight = [3, 2, 6, 4, 1]
price = [4, 1, 3, 2, 1]
listss = []


prev = [0]*(capacity+1)
listss.append(prev)
for w in range(len(weight)):
    current = []
    for i in range(capacity+1):
        if i >= weight[w]:
            temp = price[w]+prev[i-weight[w]]
        else:
            temp = 0
        if temp >= prev[i]:
            current.append(temp)
        else:
            current.append(prev[i])
    listss.append(current)
    prev = current
    print(current)

print("Items Brought : ")

itemsbrought = []
for li in range(len(listss)-1,-1,-1):
    if listss[li][capacity] > listss[li-1][capacity]:
        itemsbrought.append(li)
        capacity -= weight[li-1]
    else:
        continue
print(itemsbrought)