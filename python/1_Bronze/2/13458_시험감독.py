# 20250923_v1
# import math
# n = int(input())

# a = list(map(int,input().split())) # i번 시험장의 응시자수
# b,c = list(map(int,input().split())) # 총감이 한번에 응시 가능수 b, 부감이 한번에 응시 가능수 c

# d = 0

# for i in range(n):
#     a[i] -= b

# d = len(a)
# for i in a:
#     if i > 0 : aa = i / c; d += math.ceil(aa);

# print(d)

# 20250923_v2
import math
n = int(input())

a = list(map(int,input().split())) # i번 시험장의 응시자수
b,c = list(map(int,input().split())) # 총감이 한번에 응시 가능수 b, 부감이 한번에 응시 가능수 c
count = {}

for i in a:
    if list(count.keys()) not in i: count[i] = 0
    count[i] += 1

print(count)