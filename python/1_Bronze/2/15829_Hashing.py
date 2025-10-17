def ord_96(x):
    return ord(x)-96

l = int(input())
s = list(map(ord_96,input()))

r = 0

for i,a in enumerate(s):
    r += a*(31**i)

print(r % 1234567891)