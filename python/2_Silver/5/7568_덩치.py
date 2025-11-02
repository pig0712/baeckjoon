n = int(input())

a = []
b = [1 for _ in range(n)]

for _ in range(n):
    a.append(list(map(int,input().split())))


for i in range(n):
    for j in a:
        if (a[i][0] < j[0]) and (a[i][1] <j[1]) : b[i] += 1

print(*b) 