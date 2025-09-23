N, B = input().split()

notation = {}

for i in range(10):
    notation[str(i)] = i

for i in range(26):
    notation[chr(65+i)] = 10+i

result = 0

count = 0
for i in reversed(N):
    result += notation[i] * int(B)**count
    count += 1

print(result)