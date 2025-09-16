N, B = map(int, input().split())

notation = {}

for i in range(10):
    notation[i] = str(i)

for i in range(26):
    notation[10+i] = chr(65+i)

a = []


while N > 0:
    a.append(N % B)
    N = N // B
a.reverse()

count = 0
result = ""
for i in a:
    result += notation[i]

print(result)