## 1
# import sys

# a = sys.stdin.read().replace("\n","")

# for i in range(4):
#     if a.index(a[i])//2 != 0: print(a[i])


# 2
lst = []

for _ in range(5):
    lst.append(input())

for i in set(lst):
    if lst.count(i) % 2 != 0 : print(i)