from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = deque()
a, b = 0, 0

for _ in range(n):
    op = list(map(int, input().split()))
    if op[0] == 1:
        q.append(op[1])
    else:
        if q:
            q.popleft()

    if q:
        tail = q[-1]
        L = len(q)
        if L > a:
            a, b = L, tail
        elif L == a and tail < b:
            b = tail

print(a, b if a > 0 else 0)
