a = -99999999
b = 0
for i in range(9):
    u = int(input())

    if a < u:
        a = u
        b = i
print(a)
print(b+1)