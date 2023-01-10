#Problem at : https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20f15
import string
import random
lower = string.ascii_lowercase[:]
upper = string.ascii_uppercase[:]
pasw = input()
#Check if digit in pasw
for i in range(len(pasw)):
    if pasw[i].isdigit():
        break
    elif i == len(pasw)-1:
        pasw += '1'
#Check if lower aplha in pasw
for i in range(len(pasw)):
    if pasw[i].isalpha() and pasw[i].islower():
        break
    elif i == len(pasw)-1:
        pasw += random.choice(lower)
#Check if upper alpha in pasw
for i in range(len(pasw)):
    if pasw[i].isdigit() and pasw[i].isupper():
        break
    elif i == len(pasw)-1:
        pasw += random.choice(upper)
for i in range(len(pasw)):
    if pasw[i] in '#@*&':
        break
    elif i == len(pasw)-1:
        pasw += random.choice('#@*&')
if len(pasw) < 7:
    for i in range(7-len(pasw)):
        pasw += random.choice(lower+upper)
print(pasw)
