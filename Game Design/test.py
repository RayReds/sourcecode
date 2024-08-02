temp = ['alo','dad']
file = open('Log.txt', 'r')

temp = file.readlines()
print(temp)
for i in temp:
    print(i)
file.close()
                