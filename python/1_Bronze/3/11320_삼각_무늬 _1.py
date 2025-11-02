n = int(input())

for _ in range(n):
    a,b = list(map(int,input().split()))

    r = (a**2/2)/(b**2/2)
    if r == int(r): print(int(r))
    else : print(int(r+1))