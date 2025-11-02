from sys import stdin
input = stdin.readline


n, m = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

b = list(map(int, input().split()))


mx = []
for i in range(n):
    a = 0
    for j in range(n):
        ab = abs(A[j][i] - B[j][i])
        if a < ab : 
            a = ab 
    mx.append(a)

dic = {i : 0 for i in range(1,n+1)}
for i in b:
    dic[i] += 1 

result = 0
for i in set(b):
    result += mx[i-1] * dic[i]
print(result)