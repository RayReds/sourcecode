import re
num = input()
x = re.findall('[/*]', num)
def findAround(index):
    firstindex = 0
    secondindex = 0
    for i in range(index-1, -1, -1):
        if num[i].isdigit():
            firstindex = i
        else:
            break
    for i in range(index+1, len(num)):
        if num[i].isdigit():
            secondindex = i
        else:
            break
    return (firstindex, secondindex)
def calculate(operator):
    global num
    index = num.index(operator)
    points = findAround(index)
    firstNum = num[points[0]:index]
    secondNum = num[index+1:points[1]+1]
    if operator == '^':
        change = str(int(firstNum)**int(secondNum))
    elif operator == '*':
        change = str(int(firstNum)*int(secondNum))
    elif operator == '/':
        change = str(int(firstNum)/int(secondNum))
    elif operator == '+':
        change = str(int(firstNum)+int(secondNum))
    elif operator == '-':
        change = str(int(firstNum)-int(secondNum))
    num = num[:points[0]]+change+num[points[1]+1:]
while '^' in num:
    calculate('^')
    print(num + ' =')
for i in x:
    calculate(i)
    print(num + ' =')
x = re.findall('[-+]', num)
for i in x:
    calculate(i)
    print(num + ' =')
print(num)
