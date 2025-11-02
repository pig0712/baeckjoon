_, k = map(int,input().split())
a = list(map(int,input().split()))

c = 0
for i in range(1,len(a)):
    if a[i-1] >= a[i]:
        a[i] += k
        c += 1
        if a[i-1] >= a[i]: print(-1); exit()

print(c)