n, m = list(map(int,input().split(" ")))

lst = [0 for i in range(n)]

for i in range(m):
    a = list(map(int,input().split(" ")))

    for j in range(a[0]-1,a[1]):
        lst[j] = a[2]

for i in range(len(lst)):
    print(lst[i],end=" ")
