####################################
# 계수 정렬 사용
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

n = int(input())

numbers = {i : 0 for i in range(1,10001)}
for _ in range(n):
    a = int(input())
    numbers[a] += 1

for k,l in numbers.items():
    for _ in range(l):
        print(str(k)+"\n")
####################################