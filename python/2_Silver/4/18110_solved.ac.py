from collections import deque
from sys import stdin
input = stdin.readline
def round(n):
    if int(n) == 0:
        if n < 0.5 : return 0
        else: return 1

    elif n % int(n) < 0.5: return int(n)
    elif n % int(n) >= 0.5: return int(n)+1

n = int(input())

# 평가 수가 0이면 난이도 -> 0
# 30% 절사 평균으로 난이도 측정

if n == 0 : print(0)
else:
    sc = []

    for _ in range(n):
        sc.append(int(input()))

    sc.sort()
    sc = deque(sc)

    for _ in range(round(n*0.15)):
        sc.pop()
        sc.popleft()

    print(round(sum(sc)/(n-(round(n*0.15))*2)))