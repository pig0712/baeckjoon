n, m = list(map(int,input().split(" ")))

lst = [i+1 for i in range(n)]

for _ in range(m):
    i, j = list(map(int,input().split(" ")))

    while True:

        lst[i-1], lst[j-1] = lst[j-1], lst[i-1]

        i += 1
        j -= 1

        if (i-1 == j) or (i-1 > j):
                break
for i in lst:
    print(i, end= " ")