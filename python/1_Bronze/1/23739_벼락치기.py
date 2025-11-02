"""
5
20 -> 10 남음 case 1
40 -> 30 남고 절반 아님 case 4
60 -> 30 남고 절반임 case 3
80 -> 50 남고 아님 case 4
100 -> case 4
"""

lst = []
for _ in range(int(input())):
    lst.append(int(input()))

a = 30
c = 0
for i in lst:
    if a - i > 0: a -= i; c += 1
    elif a - i == 0 : a = 30; c += 1
    else : 
        if i - a <= i/2 : a = 30; c+= 1
        else: a = 30
print(c)