# m = int(input())
# capacity = int(input())
# values = [int(i) for i in input().split()]
# weights = [int(i) for i in input().split()]

capacity = 6
values = [3, 4, 2,3]
weights = [2, 3, 1,1]
possibilities = []
temp = []
m = len(values)
max = 0
def findMax(index, cap):
    global possibilities
    global temp
    if index < m:
        if cap > capacity:
            if index >= 1:
                possibilities = temp
                temp = []
            print(possibilities)
            findMax(index+1, 1)
        elif index == 0:
            if weights[index] <= cap:
                possibilities.append(values[index])
                findMax(index, cap+1)
            else:
                possibilities.append(0)
                findMax(index, cap+1)
        else:
            finalVal = 0
            if weights[index] <= cap:
                if cap-weights[index] > 0:
                    finalVal = values[index]
                    finalVal += possibilities[cap-weights[index]-1]
                else:
                    finalVal = values[index]
                if finalVal > possibilities[cap-1]:
                    temp.append(finalVal)
                else:
                    temp.append(possibilities[cap-1])
                findMax(index, cap+1)
            else:
                temp.append(possibilities[cap-1])
                findMax(index, cap+1)
findMax(0, 1)
print(possibilities[-1])
