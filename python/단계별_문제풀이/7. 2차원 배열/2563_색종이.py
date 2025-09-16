m = [[0 for _ in range(100)] for _ in range(100)]

for i in range(int(input())):
    a, b = map(int, input().split())
    for x in range(10):
        for y in range(10):
            m[a+x][100-b-y] = 1

count = 0
for i in m:
    for j in i:
        if j == 1 :
            count += 1

print(count)