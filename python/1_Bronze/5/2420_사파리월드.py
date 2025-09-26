a,b = list(map(int,input().split()))


if (a < 0 and b > 0) or (a > 0 and b < 0):
    print(abs(a) + abs(b))
else:
    print(abs(a - b))