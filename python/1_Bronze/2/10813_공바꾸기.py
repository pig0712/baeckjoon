n, m = list(map(int,input().split(" ")))

lst = [i+1 for i in range(n)]

for i in range(m):
    i, j = list(map(int,input().split(" ")))

    lst[i-1], lst[j-1] = lst[j-1], lst[i-1]

for i in lst:
    print(i, end= " ")