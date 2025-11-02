def fac(n):
    if n <= 1:
        return 1
    return fac(n-1) * n

n = int(input())

c = 0
for i in reversed(str(fac(n))):
    if i != "0": break
    c += 1
print(c)