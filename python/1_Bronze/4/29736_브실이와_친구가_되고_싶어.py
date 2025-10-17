from sys import stdin
input = stdin.readline


a,b = list(map(int,input().split())) # 친구 범위
k,x = list(map(int,input().split()))


# 브실이 친구가능 범위
low = k - x # 7754 - 9
high = k + x # 7754 + 9


if (b < low) or (a > high):
    print("IMPOSSIBLE")
else:
    if (a >= low) and (b <= high):
        print(b - a + 1)
    elif b <= high:
        print(high - low -(high - b) + 1)
    elif a >= low:
        print(high - low -(a - low) + 1)
    else :
        print(high - low + 1)