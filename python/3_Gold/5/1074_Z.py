import sys
input = sys.stdin.readline

n,r,c = map(int,input().split())

start = 0
for _ in range(n):
    a = (2**n/2)-1
    if (r > a) and  (c > a):
        start += (2**(n-1))**2 * 3
        r -= 2**(n-1); c -= 2**(n-1); n -= 1
    elif (r > a) and  (c <= a):
        start += (2**(n-1))**2 * 2
        r -= 2**(n-1); n -= 1
    elif (r <= a) and  (c > a):
        start += (2**(n-1))**2 * 1
        c -= 2**(n-1); n -= 1
    elif (r <= a) and  (c <= a):
        start += (2**(n-1))**2 * 0
        n -= 1

print(start)