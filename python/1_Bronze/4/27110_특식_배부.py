n = int(input())

a = list(map(int,input().split()))

for i in range(len(a)):
    if a[i] >= n: a[i] = n
print(sum(a))