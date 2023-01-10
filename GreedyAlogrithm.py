sets = [[1, 7, 3, 4],
       [4, 2, 5, 3],
       [9, 5, 1, 8]]
temp = [[0*len(sets[0])]]
def find(x, y):
    if x == None:
        top = max(sets[y])

#find(None, 0)
print(max(sets[0]))
