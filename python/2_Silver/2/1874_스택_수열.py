from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
# 찾을 순서
lst = deque([])
for _ in range(n):
    lst.append(int(input()))

storage = deque([1])
result = "+\n"
i = 2
while i < n+1: 
    if len(storage) > 0:
        if storage[-1] == lst[0] : storage.pop(); lst.popleft(); result += "-\n";
        else: storage.append(i); result += "+\n"; i += 1;
    else: storage.append(i); result += "+\n"; i += 1;
r = True
for i in list(lst):
    if len(storage) > 0:
        if storage[-1] == i: storage.pop(); lst.popleft(); result += "-\n";
        else: r = False; break
    else: break

if r == True:
    print(result[:len(result)-1])
else:
    print("NO")