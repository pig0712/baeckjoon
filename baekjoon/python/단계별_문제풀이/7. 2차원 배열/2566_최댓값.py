data = [list(map(int,input().split())) for i in range(9)]

Xmax = float("-inf")
for i in range(9):
    for j in range(9):
        if data[i][j] > Xmax:
            Xmax = data[i][j]
            a,b = i,j

print(Xmax)
print(a+1,b+1)