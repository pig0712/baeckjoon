_ = input()

N = list(map(int,input().split()))
M = list(map(int,input().split()))

P = 0

for i in N:
    P += i

for j in M:
    if j == 0: continue
    P *= j

print(P)