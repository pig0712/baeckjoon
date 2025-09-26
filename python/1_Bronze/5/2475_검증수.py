a = list(map(int,input().split()))
c = 0
for i in a:
    c += i**2

print(c%10)