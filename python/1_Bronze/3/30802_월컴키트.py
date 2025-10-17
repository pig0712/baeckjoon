import math

n = int(input())
ts = list(map(int,input().split()))
t,p = list(map(int,input().split()))

c = 0
for i in ts:
    c += math.ceil(i/t)

print(c)
print(n//p,n%p)